import datetime, time
def get_time_now():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
rows = [
    ['third', 99.99, 111, 111, 1, 'test', get_time_now()],
    ['four', 99.99, 111, 111, 1, 'test', get_time_now()]
]
print("""INSERT into work_table (project, score, build_time, run_time, generation, config, date) values {}""".format(",".join(str(tuple(i)) for i in rows)))

print("test {} hi".format('lolol'))
# print(str(tuple(s)))
# print("""INSERT INTO mailing_list (name,email) VALUES (%s)""".format(",".join(str(i) for i in rows)))