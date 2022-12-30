from django.urls import path
from app1.views import *
app_name='sir'
urlpatterns=[
    path('shikawath/',shikawath,name='shikawath'),

]