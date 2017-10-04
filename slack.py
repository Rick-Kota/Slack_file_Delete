import requests
import json
import time
import calendar
from datetime import datetime, timedelta

_token = "xxxxxxx"
_domain = "xxxxxx"

def del_time(Day):
    Set_time = str(int(time.time())-Day*86400)
    return Set_time

def files_list(Day):
    Del_time = del_time(Day)
    files_list_url = "https://slack.com/api/files.list"
    data = {"token": _token, "ts_to": Del_time, "count":1000}
    response = requests.post(files_list_url,data)
    return response.json()["files"]

def delete():

    return

if __name__ == '__main__':
    while 1:
        files = files_list(0)
        if len(files) == 0:
            print ("No files")
            break
        for f in files:
            print ("Deleting file " + f["name"] + "...")
            timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
            delete_url = "https://slack.com/api/files.delete"
            data = {
                    "token": _token,
                    "file": f["id"],
                    "set_active": "true",
                    "_attempts": "1"
                    }
            requests.post(delete_url, data)
print ("DONE!")
