#!/usr/bin/python
# Checking Error "500" response in 30 hits
import time
import requests
import sys
Url = sys.argv[1]
file1 = "/Users/Arun/python/Test-Python/Basic/Status-Code"
for x in range(0, 30):
    resp = requests.get(Url)
    print("Executing {0} {1}run".format(x))
    Status = resp.status_code
    print (Status)
    time.sleep(10)
    if Status == 500:
        with open(file1,  'w') as wf:

            wf.write("500 status code at %s  run" % x)
        time.sleep(10)
