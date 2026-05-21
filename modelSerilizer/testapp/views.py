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


    # Create Resource
    def post(self, request, *args, **kwargs):
        # data from body
        json_data = request.body
        # convert into stream
        stream = io.BytesIO(json_data)
        # JSON data into python data
        pydata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pydata)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'Resources Created sucessfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        # Print Error
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json',status=400)
    

    # Update Resource
    def put(self, request, *args, **kwargs):
        # collect he data 
        json_data = request.body
        # convert into stream
        stream = io.BytesIO(json_data)
        # JSON data into python data
        pydata = JSONParser().parse(stream)
        
        id = pydata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp,data=pydata)

        if serializer.is_valid():
            serializer.save()

            msg = {'msg':'Resources Updated Successfully!'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)


    # Partial Resource

    def patch(self, request, *args, **kwargs):
        # collect the data 
        json_data = request.body
        # convert into stream
        stream = io.BytesIO(json_data)
        # convert into python data
        pydata = JSONParser().parse(stream)

        id = pydata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=pydata, partial=True)

        if serializer.is_valid():
            serializer.save()

            msg = {'msg':'Resources Partially updated sucessfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)
        


                                                # DELETE RECORD


    def delete(self,request,*awargs,**kwargs):
        # collect data
        json_data = request.body
        # conver into stream
        stream = io.BytesIO(json_data)
        # convert into python
        pydata = JSONParser().parse(stream)

        id = pydata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg':'Resources Deleted sucessfully!'}
        # convert into json
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')