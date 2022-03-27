# import datetime
# import threading
# from apscheduler.schedulers.blocking import BlockingScheduler
# from lunar_festival import DateInfo
# import get_weather
# import interactive
# import get_pi_info
#
#
# def do_task_thread(func, *args, **kwargs):
#     t = threading.Thread(target=func, args=args, kwargs=kwargs)
#     t.setDaemon(True)
#     t.start()
#
#
# def main():
#     sched = BlockingScheduler()
#     today = datetime.datetime.today()
#     date_info = DateInfo()
#     do_task_thread(date_info.main)
#     do_task_thread(get_weather.main)
#     do_task_thread(interactive.main)
#     do_task_thread(get_pi_info.main)
#
# # 更新redis数据
#     start_date = '%s-%s-%s %s:0:2' % (today.year, today.month, today.day, today.hour)
#     sched.add_job(date_info.main, 'interval', hours=1, start_date=start_date)  # 每小时更新一次农历日期和节日
#     sched.add_job(get_weather.main, 'interval', minutes=30)  # 每30分钟更新一次天气
#     sched.add_job(interactive.main, 'interval', minutes=30)  # 每30分钟更新一次交互信息
#     sched.add_job(get_pi_info.main, 'interval', minutes=30)  # 每30分钟更新一次交互信息
#
#     # 清除redis数据
#     start_date = '%s-%s-%s 0:0:2' % (today.year, today.month, today.day)
#     sched.add_job(date_info.main, 'interval', hours=24, start_date=start_date)  # 每小时更新一次农历日期和节日
#     sched.add_job(get_weather.main, 'interval', hours=24, start_date=start_date)  # 每30分钟更新一次天气
#     sched.add_job(interactive.main, 'interval', hours=24, start_date=start_date)  # 每30分钟更新一次交互信息
#
#     sched.start()
#
#
# if __name__ == '__main__':
#     main()

import time
import multiprocessing
from proxypool.processors.server import app
from proxypool.processors.getter import Getter
from proxypool.processors.tester import Tester
from proxypool.setting import APP_PROD_METHOD_GEVENT, APP_PROD_METHOD_MEINHELD, APP_PROD_METHOD_TORNADO, CYCLE_GETTER, \
    CYCLE_TESTER, API_HOST, \
    API_THREADED, API_PORT, ENABLE_SERVER, IS_PROD, APP_PROD_METHOD, \
    ENABLE_GETTER, ENABLE_TESTER, IS_WINDOWS
from loguru import logger

if IS_WINDOWS:
    multiprocessing.freeze_support()

tester_process, getter_process, server_process = None, None, None


class Scheduler:
    """
    scheduler
    """

    def run_tester(self, cycle=CYCLE_TESTER):
        """
        run tester
        """
        if not ENABLE_TESTER:
            logger.info('tester not enabled, exit')
            return
        tester = Tester()
        loop = 0
        while True:
            logger.debug(f'tester loop {loop} start...')
            tester.run()
            loop += 1
            time.sleep(cycle)

    def run_getter(self, cycle=CYCLE_GETTER):
        """
        run getter
        """
        if not ENABLE_GETTER:
            logger.info('getter not enabled, exit')
            return
        getter = Getter()
        loop = 0
        while True:
            logger.debug(f'getter loop {loop} start...')
            getter.run()
            loop += 1
            time.sleep(cycle)

    def run_server(self):
        """
        run server for api
        """
        if not ENABLE_SERVER:
            logger.info('server not enabled, exit')
            return
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
        global tester_process, getter_process, server_process
        try:
            logger.info('starting proxypool...')
            if ENABLE_TESTER:
                tester_process = multiprocessing.Process(
                    target=self.run_tester)
                logger.info(f'starting tester, pid {tester_process.pid}...')
                tester_process.start()

            if ENABLE_GETTER:
                getter_process = multiprocessing.Process(
                    target=self.run_getter)
                logger.info(f'starting getter, pid {getter_process.pid}...')
                getter_process.start()

            if ENABLE_SERVER:
                server_process = multiprocessing.Process(
                    target=self.run_server)
                logger.info(f'starting server, pid {server_process.pid}...')
                server_process.start()

            tester_process and tester_process.join()
            getter_process and getter_process.join()
            server_process and server_process.join()
        except KeyboardInterrupt:
            logger.info('received keyboard interrupt signal')
            tester_process and tester_process.terminate()
            getter_process and getter_process.terminate()
            server_process and server_process.terminate()
        finally:
            # must call join method before calling is_alive
            tester_process and tester_process.join()
            getter_process and getter_process.join()
            server_process and server_process.join()
            logger.info(
                f'tester is {"alive" if tester_process.is_alive() else "dead"}')
            logger.info(
                f'getter is {"alive" if getter_process.is_alive() else "dead"}')
            logger.info(
                f'server is {"alive" if server_process.is_alive() else "dead"}')
            logger.info('proxy terminated')


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()
