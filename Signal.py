import json
import time
import traceback
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from config import *
from apscheduler.schedulers.background import BackgroundScheduler
from SignalUtils import *

def get_account():
    try:
        resp = get_alpha_account()['accounts']
        result = select_token_to_liquidate_by_account(
            resp,
            token_filter='cETH',
            balance_threshold=2
        )
        print(json.dumps(result, indent=4))
    except:
        error = traceback.format()
        print(error)


scheduler = BackgroundScheduler()
crontab_expression = '* * * * *' # every minute
scheduler.add_job(get_account, CronTrigger.from_crontab(crontab_expression))
scheduler.start()

while True:
    time.sleep(1)