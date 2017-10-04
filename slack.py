# Please Serch Your Slack User ID in https://api.slack.com/methods/users.list
# Please taken Your Slack Token in https://api.slack.com/custom-integrations/legacy-tokens

import requests
import json
import time
import sys

# Load JSON file
file = open('Setting.json', 'r')
Setting = json.load(file)
file.close()
_token = Setting["token"]
_domain = Setting["domain"]
_ID = Setting["User"][0]["name"]

# init
_Delete_url = "https://slack.com/api/files.delete"
_List_url = "https://slack.com/api/files.list"

# make timestamp filter
def del_time(Day):
    Set_time = str(int(time.time())-Day*86400) #(24*60*60=86400)
    return Set_time

# Get Filelist
def files_list(Day):
    # Check access permission from "Setting.json"
    if Setting["User"][0]["admin"]:
        user = None
    else: # When not have Administrator's authority
        user = _ID
    data = {
        "token": _token, "ts_to": del_time(Day), "count": 500, "user":user
        }
    response = requests.post(_List_url,data)
    # Check Error If you have problem in "token" or "domain" or "userID" and etc...
    # then stop in next " sys.exit() "
    if response.json()["ok"] == 0:
        print("Error_exit(around API's argument)")
        sys.exit()
    return response.json()["files"]

# Not making now
def delete():
    
    return

if __name__ == '__main__':
    while True:
        # Checking about finshed delet files
        if len(files_list(int(Setting["Day"]))) == False:
            print ("No files")
            break
        for f in files_list(int(Setting["Day"])):
            print ("Processing >> " + f["name"] + "...") # Show Proccessing files name
            data = {
                "token": _token, "file": f["id"], "set_active": "true", "_attempts": "1"
                    }
            requests.post(_Delete_url, data)# Send delete comand to API
print ("complete")
# end
