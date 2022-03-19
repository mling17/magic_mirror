from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import time


def job_function():
    print("Hello World", time.ctime())


today = datetime.today()
schedule = BlockingScheduler()
print('--->', time.ctime())
start_date = '%s-%s-%s %s:30:1' % (today.year, today.month, today.day, today.hour)
schedule.add_job(job_function, 'interval', minutes=10, start_date=start_date)
schedule.start()
