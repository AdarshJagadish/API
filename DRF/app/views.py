from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializer import *

# def fun1(request):
#     if request.method=='GET':
#         data = stud.objects.all()
#         s=studSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)
    
    
# @csrf_exempt
# def fun1(request):
#     if request.method=='GET':
#         data=stud.objects.all()
#         s=studModelSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)
#     elif request.method=='POST':
#         d=JSONParser().parse(request)
#         s=studModelSerializer(data=d)
#         print(s)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data,safe=False)
#         else:
#             return JsonResponse(s.errors)
        
        
@csrf_exempt
def fun1(request,pk):
    try:
        demo=stud.objects.get(pk=pk)
        print('helo')
    except:
        return HttpResponse("Invalid")
    if request.method=='GET':
        s=studModelSerializer(demo)
        return JsonResponse(s.data)
    
# Create your views here.
