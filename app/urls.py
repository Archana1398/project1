from django.urls import path
from app.views import*
app_name='anything'

urlpatterns=[
    path('first/',first,name='first')
    
]