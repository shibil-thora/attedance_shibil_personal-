from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response 
from firebase_admin import credentials, db 
import firebase_admin 
import datetime

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://marketing-data-d141d-default-rtdb.firebaseio.com'
})


class GetEmployees(APIView): 
    def get(self, request):  
        data = {
            'name': 'Onwords', 
            'place': 'chinniyampalayam', 
            'state': 'Tamilnadu', 
            'time': datetime.datetime.now()
        }
        return Response('hi from shibil')