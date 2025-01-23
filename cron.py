import random
from datetime import datetime
now = datetime.now()
num = random.randint(1, 101)
with open('/home/ubuntu/flask-ms/cron/rand.txt', 'a') as f:
    f.write('{} - Your random number is {}\n'.format(now, num))