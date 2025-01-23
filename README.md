Crontab Syntax
The crontab syntax is very powerful and flexible.  Below is a reference describing the syntax for a cronjob i.e. a single line in the crontab file.

┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
│ │ │ │ │                                   7 is also Sunday on some systems)
│ │ │ │ │
│ │ │ │ │
* * * * * command to executeFrom left to right, each of the 5 asterisks represents minute, hour, day of month, month, and  day of week.


Schedule a Python Script with Crontab

Open the crontab file.
  crontab -e

* * * * * /usr/bin/python3 /test/cron.py
