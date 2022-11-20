import requests
import json
URL = "http://127.0.0.1:8000/studentapi"

def get_data(id =None):
 data ={'gopal'}
if id is not None:
    data = {'id':id}
    json_data = json.dumps(data)
    r= requests.post(url=URL, data= json_data)
    data= r.json()
    print (data)

get_data()