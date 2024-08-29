from django.urls import path 
from . import views

urlpatterns = [
    path('get_employees/', views.GetEmployees.as_view())
]
