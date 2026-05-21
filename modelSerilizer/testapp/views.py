from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from testapp.models import Employee
from testapp.serializations import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your business logic / views here.

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):

    # GET 
    def get(self, request, *args, **kwargs):
        # data from body
        json_data = request.body
        # convert into stream
        stream = io.BytesIO(json_data)
        # JSON data into python data
        pydata = JSONParser().parse(stream)

        id = pydata.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            eserializer = EmployeeSerializer(emp)
            # conver into JSON data
            json_data = JSONRenderer().render(eserializer.data)

            return HttpResponse(json_data, content_type='application/json', status=200)
        # If ot come then this
        qurey_set = Employee.objects.all()
        eserializer = EmployeeSerializer(qurey_set, many=True)
        json_data = JSONRenderer().render(eserializer.data)
        return HttpResponse(json_data,content_type='application/json')

    