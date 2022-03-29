from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import schedule
import threading
from lunar_festival import DateInfo
import get_weather
import interactive

# schedule.every().hours.do(do_task_thread, date_info.main)  # 每小时更新一次农历日期和节日
# schedule.every(30).minutes.do(do_task_thread, get_weather.main)  # 每30分钟更新一次天气
# schedule.every(30).minutes.do(do_task_thread, interactive.main)  # 每30分钟更新一次交互信息

sched = BlockingScheduler()

today = datetime.today()

date_info = DateInfo()
start_date = '%s-%s-%s %s:%s:%s' % (today.year, today.month, today.day, today.hour, today.minute, today.second)
sched.add_job(date_info.run, 'interval', hours=1, start_date=start_date)  # 每小时更新一次农历日期和节日
sched.add_job(get_weather.run, 'interval', minutes=30)  # 每30分钟更新一次天气
sched.add_job(interactive.run, 'interval', minutes=30)  # 每30分钟更新一次交互信息
# 清理redis数据
start_date = '%s-%s-%s 0:0:2' % (today.year, today.month, today.day)
sched.add_job(date_info.run, 'interval', hours=24, start_date=start_date)
sched.start()
