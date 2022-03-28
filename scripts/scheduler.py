import multiprocessing
from loguru import logger
from processor.pi import PiRun
from processor.get_weather import Weather
from settings import ENABLE_PI, ENABLE_WEATHER

pi_process, weather_process = None, None


class Scheduler(object):
    """
    scheduler
    """

    def run_pi(self):
        PiRun().run()

    def run_weather(self):
        if ENABLE_WEATHER:
            Weather().run()
        else:
            logger.info('Weather information module is disable.')

    # def run_server(self):
    #     """
    #     run server for api
    #     """
    #     if not ENABLE_SERVER:
    #         logger.info('server not enabled, exit')
    #         return
    #     if IS_PROD:
    #         if APP_PROD_METHOD == APP_PROD_METHOD_GEVENT:
    #             try:
    #                 from gevent.pywsgi import WSGIServer
    #             except ImportError as e:
    #                 logger.exception(e)
    #             else:
    #                 http_server = WSGIServer((API_HOST, API_PORT), app)
    #                 http_server.serve_forever()
    #
    #         elif APP_PROD_METHOD == APP_PROD_METHOD_TORNADO:
    #             try:
    #                 from tornado.wsgi import WSGIContainer
    #                 from tornado.httpserver import HTTPServer
    #                 from tornado.ioloop import IOLoop
    #             except ImportError as e:
    #                 logger.exception(e)
    #             else:
    #                 http_server = HTTPServer(WSGIContainer(app))
    #                 http_server.listen(API_PORT)
    #                 IOLoop.instance().start()
    #
    #         elif APP_PROD_METHOD == APP_PROD_METHOD_MEINHELD:
    #             try:
    #                 import meinheld
    #             except ImportError as e:
    #                 logger.exception(e)
    #             else:
    #                 meinheld.listen((API_HOST, API_PORT))
    #                 meinheld.run(app)
    #
    #         else:
    #             logger.error("unsupported APP_PROD_METHOD")
    #             return
    #     else:
    #         app.run(host=API_HOST, port=API_PORT, threaded=API_THREADED)

    def run(self):
        global pi_process, weather_process
        try:
            logger.info('starting magic mirror...')
            if ENABLE_PI:
                pi_process = multiprocessing.Process(
                    target=self.run_pi)
                logger.info(f'starting tester, pid {pi_process.pid}...')
                pi_process.start()
            else:
                logger.info('Pi functions is disable.')

            if ENABLE_WEATHER:
                weather_process = multiprocessing.Process(
                    target=self.run_weather)
                logger.info(f'starting weather module, pid {weather_process.pid}...')
                weather_process.start()
            else:
                logger.info('Weather information module is disable.')

            # if ENABLE_SERVER:
            #     server_process = multiprocessing.Process(
            #         target=self.run_server)
            #     logger.info(f'starting server, pid {server_process.pid}...')
            #     server_process.start()

            pi_process and pi_process.join()
            weather_process and weather_process.join()
            # server_process and server_process.join()
        except KeyboardInterrupt:
            logger.info('received keyboard interrupt signal')
            pi_process and pi_process.terminate()
            weather_process and weather_process.terminate()
            # server_process and server_process.terminate()
        finally:
            # must call join method before calling is_alive
            pi_process and pi_process.join()
            weather_process and weather_process.join()
            # server_process and server_process.join()
            logger.info(
                f'tester is {"alive" if pi_process.is_alive() else "dead"}')
            logger.info(
                f'getter is {"alive" if weather_process.is_alive() else "dead"}')
            # logger.info(
            #     f'server is {"alive" if server_process.is_alive() else "dead"}')


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()
