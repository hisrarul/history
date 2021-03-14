import os
import time
import sys

while True:
    try:
        print("Started hadoop alert script")
        os.system('python hadoopAlert.py')
        print("Sleeping for 2 minute")
        time.sleep(120)
    except Exception as e:
        print(e)