from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from playwright_task import run_playwright
import time
import datetime

scheduler = BlockingScheduler()


def scheduler():
    #controller = di.get_controller()
    #controller.download()
    scheduler.add_job(
        run_playwright,
        trigger=CronTrigger.from_crontab("* * * * *"),
        max_instances=1
    )

def start_scheduler():
    scheduler.start()
