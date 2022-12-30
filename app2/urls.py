from django.urls import path
from app2.views import *
app_name='raj'
urlpatterns=[
    path('pushpa/',pushpa,name='pushpa'),
]