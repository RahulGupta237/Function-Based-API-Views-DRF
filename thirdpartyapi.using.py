import requests,json

URL='http://127.0.0.1:8000/apitest/'

def get_data(id=None):
    data={}
    headers={"content-Type":"application/json"}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)





def post_data():
    
    data={
        
        'name':'Tara',
        'city':'Kodad',
        'roll':237,
        
    }
    headers={"content-Type":"application/json"}
    json_data=json.dumps(data)
    print(json_data)

    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# def put_data():
def update_data():
    
    data={
        'id':1,
        'name':'Shabnam',
        'city':'Raxaul',
        'roll':237,
        
    }
    headers={"content-Type":"application/json"}

    json_data=json.dumps(data)
    print(json_data)

    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)


def delete_data():
    
    data={
        'id':8,
       
        
    }

    headers={"content-Type":"application/json"}

    json_data=json.dumps(data)
    print(json_data)

    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

#post_data()
# get_data()  # Read
delete_data() # Update
#put_data() # Delete
# update_data()





