#from django.conf.urls import url 

from django.urls import re_path as url

from app2 import views

urlpatterns=[
    url(r'^$',views.user,name='user')
]