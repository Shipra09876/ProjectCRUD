from django.shortcuts import render
from .models import *
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import status,parsers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


def index(request):
    return render(request,'student_list.html')

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        # In a GET request, request.body should not be used to extract query parameters. Instead, query parameters should be accessed using request.GET.

        # fetch the id from db 
        student_id = request.GET.get('id')
        if student_id:
            try:
                # follow 3 steps 
                '''
                function based veiws 
                get the mentioned id data from db
                serialized it 
                Response the serialized data 
                if doesn't exist the model then throw the error 

                and if id's not mentioned then fetch all query set and serialized it and response it 
                '''
                student = Student.objects.get(id=student_id)
                serializer = StudentSerializers(student) 
                return JsonResponse(serializer.data, safe=False)
            
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
        else:
            students = Student.objects.all()
            serializer = StudentSerializers(students, many=True)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        # The request.body is used primarily for POST and PUT requests, where the data is sent in the request body as JSON. For GET requests, parameters are usually sent in the query string.

        '''
        First i get the data from body serialized the data and paarse it and check the vailidity if valid then store into db 
        ''' 
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = parsers.JSONParser().parse(stream)
        serializer = StudentSerializers(data=python_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data created'}, status=201)

        return JsonResponse(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = parsers.JSONParser().parse(stream)
        student_id = python_data.get('id', None)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

        serializer = StudentSerializers(student, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data updated'})

        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = parsers.JSONParser().parse(stream)
        student_id = python_data.get('id', None)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

        student.delete()
        return JsonResponse({'msg': 'Data deleted'})

