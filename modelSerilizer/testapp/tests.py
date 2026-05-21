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
print("="*30)
print()


# Create Resources from DataBase
def create_resource():
    new_emp = {

        'emp_id':103,
        'emp_name':'Salman Khan',
        'emp_sal':78000,
        'emp_add':'Bandra',
    }
    # Conver into JSON
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

create_resource()