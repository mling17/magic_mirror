import multiprocessing
from loguru import logger

from processor.get_weather import Weather
from processor.server import app
from processor.lunar_festival import DateInfo
from processor.redis_conn import RedisClient
from settings import ENABLE_PI, ENABLE_WEATHER, ENABLE_SERVER, ENABLE_LUNAR, APP_PROD_METHOD_GEVENT, \
    APP_PROD_METHOD_TORNADO, APP_PROD_METHOD_MEINHELD, IS_PROD, APP_PROD_METHOD, API_HOST, API_PORT, API_THREADED, \
    ENVIRONMENT
if ENVIRONMENT.lower() == 'pi':
    from processor.pi import PiRun
else:
    ENABLE_PI = False

pi_process, weather_process, lunar_process, server_process = None, None, None, None


class Scheduler(object):
    """
    scheduler
    """

    def __init__(self):
        r = RedisClient().db
        for key in r.keys():
            r.delete(key)

    def run_pi(self):
        PiRun().run()

    def run_weather(self):
        Weather().run()

    def run_lunar(self):
        DateInfo().run()

    def run_server(self):
        """
        run server for api
        """
        if IS_PROD:
            if APP_PROD_METHOD == APP_PROD_METHOD_GEVENT:
                try:
                    from gevent.pywsgi import WSGIServer
                except ImportError as e:
                    logger.exception(e)
                else:
                    http_server = WSGIServer((API_HOST, API_PORT), app)
                    http_server.serve_forever()

            elif APP_PROD_METHOD == APP_PROD_METHOD_TORNADO:
                try:
                    from tornado.wsgi import WSGIContainer
                    from tornado.httpserver import HTTPServer
                    from tornado.ioloop import IOLoop
                except ImportError as e:
                    logger.exception(e)
                else:
                    http_server = HTTPServer(WSGIContainer(app))
                    http_server.listen(API_PORT)
                    IOLoop.instance().start()

            elif APP_PROD_METHOD == APP_PROD_METHOD_MEINHELD:
                try:
                    import meinheld
                except ImportError as e:
                    logger.exception(e)
                else:
                    meinheld.listen((API_HOST, API_PORT))
                    meinheld.run(app)

            else:
                logger.error("unsupported APP_PROD_METHOD")
                return
        else:
            app.run(host=API_HOST, port=API_PORT, threaded=API_THREADED)

    def run(self):
        global pi_process, weather_process, lunar_process, server_process
        try:
            logger.info('starting magic mirror...')
            if ENABLE_PI:
                pi_process = multiprocessing.Process(target=self.run_pi)
                logger.info(f'starting tester, pid {pi_process.pid}...')
                pi_process.start()
            else:
                logger.info('Pi functions module is disable.')

            if ENABLE_WEATHER:
                weather_process = multiprocessing.Process(target=self.run_weather)
                logger.info(f'starting weather module, pid {weather_process.pid}...')
                weather_process.start()
            else:
                logger.info('Weather information module is disable.')

            if ENABLE_LUNAR:
                lunar_process = multiprocessing.Process(target=self.run_lunar)
                logger.info(f'starting lunar module, pid {lunar_process.pid}...')
                lunar_process.start()
            else:
                logger.info('Weather information module is disable.')

            if ENABLE_SERVER:
                server_process = multiprocessing.Process(target=self.run_server)
                logger.info(f'starting server, pid {server_process.pid}...')
                server_process.start()
            else:
                logger.info('Server module is disable.')

            pi_process and pi_process.join()
            weather_process and weather_process.join()
            lunar_process and lunar_process.join()
            server_process and server_process.join()
        except KeyboardInterrupt:
            logger.info('received keyboard interrupt signal')
            pi_process and pi_process.terminate()
            weather_process and weather_process.terminate()
            lunar_process and lunar_process.terminate()
            server_process and server_process.terminate()
        finally:
            # must call join method before calling is_alive
            pi_process and pi_process.join()
            weather_process and weather_process.join()
            lunar_process and lunar_process.join()
            server_process and server_process.join()
            logger.info(
                f'pi_process is {"alive" if pi_process and pi_process.is_alive() else "dead"}')
            logger.info(
                f'weather_process is {"alive" if weather_process and weather_process.is_alive() else "dead"}')
            logger.info(
                f'lunar_process is {"alive" if lunar_process and lunar_process.is_alive() else "dead"}')
            logger.info(
                f'server_process is {"alive" if server_process and server_process.is_alive() else "dead"}')


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()
