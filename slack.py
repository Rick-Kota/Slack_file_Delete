import requests
import json
import time
import calendar
from datetime import datetime, timedelta

_token = "xxxx"
_domain = "xxxxx"

def del_time(Day):
    Set_time = Day*24*60*60
    return Set_time

def files_list(Day):
    Del_time = (time.time()) - del_time(Day)
    files_list_url = "https://slack.com/api/files.list?token=" + _token +"&pretty=1"
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
            delete_url = "https://" + _domain + ".slack.com/api/files.delete?t=" + timestamp
            requests.post(delete_url, data = {
              "token": _token,
              "file": f["id"],
              "set_active": "true",
              "_attempts": "1"})
print ("DONE!")
