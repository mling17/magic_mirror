import datetime
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from lunar_festival import DateInfo
import get_weather
import interactive
import get_pi_info


def do_task_thread(func, *args, **kwargs):
    t = threading.Thread(target=func, args=args, kwargs=kwargs)
    t.setDaemon(True)
    t.start()


def main():
    sched = BlockingScheduler()
    today = datetime.datetime.today()
    date_info = DateInfo()
    do_task_thread(date_info.main)
    do_task_thread(get_weather.main)
    do_task_thread(interactive.main)
    do_task_thread(get_pi_info.main)

# 更新redis数据
    start_date = '%s-%s-%s %s:0:2' % (today.year, today.month, today.day, today.hour)
    sched.add_job(date_info.main, 'interval', hours=1, start_date=start_date)  # 每小时更新一次农历日期和节日
    sched.add_job(get_weather.main, 'interval', minutes=30)  # 每30分钟更新一次天气
    sched.add_job(interactive.main, 'interval', minutes=30)  # 每30分钟更新一次交互信息
    sched.add_job(get_pi_info.main, 'interval', minutes=30)  # 每30分钟更新一次交互信息

    # 清除redis数据
    start_date = '%s-%s-%s 0:0:2' % (today.year, today.month, today.day)
    sched.add_job(date_info.main, 'interval', hours=24, start_date=start_date)  # 每小时更新一次农历日期和节日
    sched.add_job(get_weather.main, 'interval', hours=24, start_date=start_date)  # 每30分钟更新一次天气
    sched.add_job(interactive.main, 'interval', hours=24, start_date=start_date)  # 每30分钟更新一次交互信息

    sched.start()


if __name__ == '__main__':
    main()
