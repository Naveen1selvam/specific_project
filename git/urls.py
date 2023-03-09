from git.views import *
from django.urls import path 
app_name='something'
urlpatterns=[
    path('git/',git,name='git'),
]