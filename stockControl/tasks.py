import os
from huey import SqliteHuey
from huey import crontab

huey = SqliteHuey(filename='/tmp/huey.db')

@huey.periodic_task(crontab(minute='*/1'))
def every_minute():
    print('This task runs every minute')
