from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response 
import datetime


class GetEmployees(APIView): 
    def get(self, request):  
        data = {
            'name': 'Onwords', 
            'place': 'chinniyampalayam', 
            'state': 'Tamilnadu', 
            'time': datetime.datetime.now()
        }
        return Response(data)