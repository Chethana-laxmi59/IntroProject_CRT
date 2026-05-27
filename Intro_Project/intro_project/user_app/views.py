from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# http://127.0.0.1:8000/user/message

def greet(request):
    return HttpResponse("Hii,Good Morning")

def get_name(request):
    return HttpResponse("Hello Chethana")

def details(request):
    return HttpResponse([{"name":"Chethana",
                         "email":"Chethana@gmail.com",
                         "phone":"1234567890"},
                        {"name":"Ruksana",
                         "email":"Ruksana@gmail.com",
                         "phone":"9987654321"},
                        {"name":"Thanuja",
                         "email":"Thanuja@gmail.com",
                         "phone":"9678012345"},
                        {"name":"Stephy",
                         "email":"Stephy@gmail.com",
                         "phone":"4356789012"}])


"""
    http://127.0.0.1:8000/user/data
[
    {
        "name":"",
        "email":"",
        "address":"",
    }
]
"""

def greet_to_user(request,name,age):
    return HttpResponse(f"Hii,{name} Good Morning\n"
                        f"Your age is {age}")