import requests
import json
import time
import calendar
from datetime import datetime, timedelta

_token = "xoxp-35468490069-35470635781-250500842112-dcea281a55939480c6e068783ddba152"
_domain = "wanglab-cit-team"

def del_time(Day):
    Set_time = Day*24*60*60
    return Set_time

Del_time = (time.time()) - del_time(10)
if __name__ == '__main__':
    while 1:
        files_list_url = "https://slack.com/api/files.list?token=" + _token +"&pretty=1"
        data = {"token": _token, "ts_to": Del_time}
        response = requests.get(files_list_url)
        if len(response.json()["files"]) == 0:
           break
        for f in response.json()["files"]:
           print "Deleting file " + f["name"] + "..."
           timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
           delete_url = "https://" + _domain + ".slack.com/api/files.delete?t=" + timestamp
           requests.post(delete_url, data = {
                         "token": _token,
                         "file": f["id"],
                         "set_active": "true",
                         "_attempts": "1"})
print "DONE!"

