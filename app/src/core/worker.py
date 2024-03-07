import time
from celery import Celery
import pymysql
from dotenv import load_dotenv
import os
import ipdata
import json
pymysql.install_as_MySQLdb()
load_dotenv()


celery = Celery('celeryconfig', broker=os.getenv('CELERY_BROKER_URL'), backend=os.getenv('CELERY_RESULT_BACKEND_URL'))
celery.autodiscover_tasks()

@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@celery.task(name="get_ip_info")
def get_ip_info(ip):
    ipdata.api_key = os.getenv('IPDATA_API_KEY')
    response = ipdata.lookup(ip)
    response_json = json.dumps(response)
    return response_json