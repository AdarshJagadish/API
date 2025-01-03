from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .serializer import *

def fun1(request):
    if request.method=='GET':
        data = stud.objects.all()
        s=studSerializer(data,many=True)
        return JsonResponse(s.data,safe=False)
# Create your views here.
