#!/usr/bin/python
# Checking Error "500" response in 30 hits
import time
import requests
Url = "http://N7PRPDVALAMP0{1,3,4}:8180"
for x in range(0, 30):
    resp = requests.get(Url)
    print("Executing {} run".format(x))
    Status = resp.status_code
    print (Status)
    time.sleep(10)
    if Status == 500:
        print("500 error at {} run".format(x))
        time.sleep(5)
