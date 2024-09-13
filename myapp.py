# how to get the API to external application fetch the api and response the data 
# this app communicate to api and fetch the data 

'''
--> For fetching the data from the API key from database to client  ('get')
'''
import requests
import json
# URL= 'http://127.0.0.1:8000/stuinfo/'
# r=requests.get(url=URL)
# data=r.json()
# print(data)


# '''
# --> For dumping the data from client application to database ('POST')
# '''
# URL1='http://127.0.0.1:8000/stucreate/'
# data={
#     'name':'Shipra',
#     'roll_no':102,
#     'city':'Alwar'
# }
# # convert json data into python objects
# json_data=json.dumps(data)
# # print(json_data)
# s=requests.post(url=URL1,data=json_data)
# data=s.json()
# print(data)


import requests
import json
URL2='http://127.0.0.1:8000/api/studentapi/'
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    
    json_data=json.dumps(data)
    r=requests.get(url=URL2,data=json_data)
    data=r.json()
    print(data)

# get_data()

def post_data():
    data={
        'name':'Kunal',
        'roll_no':'4',
        'city':'pilibanga'
    }

    json_data=json.dumps(data)
    r=requests.post(url=URL2,data=json_data)
    data=r.json()
    print(data)

post_data()


def update_data():
    data={
        'id':23,
        'name':'Jaanu',
        'city':'Delhi'
    }

    json_data=json.dumps(data)
    r=requests.put(url=URL2,data=json_data)
    data=r.json()
    print(data)

# update_data()

def delete_data():
    data={
        'id':16
    }

    json_data=json.dumps(data)
    r=requests.delete(url=URL2,data=json_data)
    data=r.json()
    print(data)

# delete_data()