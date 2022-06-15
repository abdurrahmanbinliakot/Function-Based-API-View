from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET","POST"])
def func_api_data(request):
    if request.method == "POST":
        name =request.data['name']
        age =request.data['age']
        email =request.data['email']
        return Response({"name":name,"age":age,"email":email})
    if request.method == "GET":
        context={
            "name":"Abdur Rahman",
            "email": "something@gmail.com"
        }

        return Response(context)
