
from django.urls import path
from django.views.generic import detail

from .views import greet,get_name,details,greet_to_user
# http://127.0.0.1:8000/user/message
# http://127.0.0.1:8000/user/name
# http://127.0.0.1:8000/user/data


urlpatterns = [
    path('message', greet),
    path('name',get_name),
    path('data',details),
    path("user_message/<str:name>/<int:age>",greet_to_user), # /user/user_message/anynameourwish
]
