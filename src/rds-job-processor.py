import boto3, json, MySQLdb, atexit, datetime, time
from os import path
from pathlib import Path
home = str(Path.home())
with open(path.join(home, '.aws/annhouga_db')) as f:
    dbpassword = f.read()

db = MySQLdb.connect(
    host="annhouga-main.czbydqdgzi5u.us-east-1.rds.amazonaws.com",
    user="josephweidinger",
    passwd=dbpassword,
    db="annhouga"
)

sqs = boto3.resource('sqs')
rds_job_queue = sqs.get_queue_by_name(QueueName='annhouga-rds-jobs')
atexit.register(lambda: db.close())
cur = db.cursor()

def get_time_now():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def transform_message_to_row_format(m):
    return [
        'first',
        round(m['loss'], 4),
        round(m['accuracy'], 4),
        round(m['run_time'], 2),
        1,
        str(m['config']),
        get_time_now()
    ]

def add_processed_nn_jobs_to_db(rows):
    statement = """INSERT into work_table (project, loss, accuracy, run_time, generation, config, date) values {};""".format(",".join(str(tuple(i)) for i in rows))
    cur.execute(statement)
    db.commit()

while 1:
    print('[*] Waiting for rds jobs. To exit press CTRL+C')
    messages = rds_job_queue.receive_messages(WaitTimeSeconds=20, MaxNumberOfMessages=10)
    num_messages = len(messages)
    if num_messages > 0:
        print('  - adding {} messages'.format(num_messages))
        rows = [transform_message_to_row_format(json.loads(message.body)) for message in messages]
        add_processed_nn_jobs_to_db(rows)

        [message.delete() for message in messages]

