from django.test import TestCase
import json, requests

# Create your tests here.
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


# Fetch Data from DataBase
def get_resource(id=None):
    data = {}

    if id is not None:
        data = {
            'id':id
        }
    resp = requests.get(BASE_URL + END_POINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

get_resource(2)
#get_resource()  # # If i am not passing any id it will fetch all the records

print()
print("="*45)
print()


                                # Create Resources from DataBase

def create_resource():
    new_emp = {
        'emp_id':104,
        'emp_name':'Sajjad',
        'emp_sal':80000,
        'emp_add':'Mumbra',
    }
    # Conver into JSON
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json)

create_resource()



print()
print("*"*45)
print()



# Update resource
def update_resource(id):
    update_emp = {
        'id':id,
        'emp_id':102,
        'emp_name':'sajju',
        'emp_sal':455000,
        'emp_add':'Mumbra'

    }
    resp = requests.put(BASE_URL + END_POINT,data=json.dumps(update_emp))
    print(resp.status_code)
    print(resp.json())

update_resource(2)  # id



print()
print("~"*45)
print()



#                                                Partial Update

def partial_resources(id):
    partial_emp = {
        'id':id,
        'emp_id':102,
        'emp_name':'sana',
        'emp_sal':455000,
        'emp_add':'Mumbra'
    }
    resp = requests.put(BASE_URL + END_POINT, data=json.dumps(partial_emp))
    print(resp.status_code)
    print(resp.json())

partial_resources(17)  # id





print()
print("~"*45)
print()



                                                # DELETE RECORD

def delete_resource(id):
    data = {
        'id':id
    }
    resp = requests.delete(BASE_URL + END_POINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

delete_resource(18)  # id


