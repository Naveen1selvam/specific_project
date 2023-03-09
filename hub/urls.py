from hub.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('hub/',hub,name='hub'),
]