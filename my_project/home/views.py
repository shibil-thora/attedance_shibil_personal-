from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response

class GetEmployees(APIView): 
    def get(self, request): 
        return Response('hi from shibil')