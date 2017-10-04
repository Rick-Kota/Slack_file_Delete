import requests
import json
import time
import sys

file = open('Setting.json', 'r')
Setting = json.load(file)
file.close()
_token = Setting["token"]
_domain = Setting["domain"]
_ID = Setting["User"][0]["name"]

def del_time(Day):
    Set_time = str(int(time.time())-Day*86400)
    return Set_time

def files_list(Day):
    Del_time = del_time(Day)
    files_list_url = "https://slack.com/api/files.list"
    print(Setting["User"][0]["admin"] )
    if Setting["User"][0]["admin"]:
        user = None
    else:
        user = _ID
    data = {
        "token": _token,
        "ts_to": Del_time,
        "count":1000,
        "user":user
        }
    response = requests.post(files_list_url,data)

    if response.json()["ok"] == 0:
        print("Error_exit(around API's argument)")
        sys.exit()
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
            delete_url = "https://slack.com/api/files.delete"
            data = {
                    "token": _token,
                    "file": f["id"],
                    "set_active": "true",
                    "_attempts": "1"
                    }
            requests.post(delete_url, data)
print ("complete")

