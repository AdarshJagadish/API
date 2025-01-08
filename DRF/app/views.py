from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializer import *

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import generics,mixins


#/-------------------------------------------------------------------------------------------------------\
#     ******************************************** POST *********************************************
#\-------------------------------------------------------------------------------------------------------/


# def fun1(request):
#     if request.method=='GET':
#         data = stud.objects.all()
#         s=studSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)
    
    
#/-------------------------------------------------------------------------------------------------------\
#     ******************************************** POST *********************************************
#\-------------------------------------------------------------------------------------------------------/


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
        

        
#/-------------------------------------------------------------------------------------------------------\
#     ******************************************** PUT **********************************************
#\-------------------------------------------------------------------------------------------------------/



# @csrf_exempt
# def fun1(request,pk):
#     try:
#         demo=stud.objects.get(pk=pk)
#         # print('helo')
#     except:
#         return HttpResponse("Invalid")                      
#     if request.method=='GET':                                      
#         s=studModelSerializer(demo)                         
#         return JsonResponse(s.data)
#     elif request.method=='PUT':
#         d=JSONParser().parse(request)
#         s=studModelSerializer(demo,data=d)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data)
#         else:
#             return JsonResponse(s.errors)


#/-------------------------------------------------------------------------------------------------------\
#     ******************************************** DELETE *********************************************
#\-------------------------------------------------------------------------------------------------------/

        
# @csrf_exempt
# def fun1(request,pk):
#     try:
#         demo=stud.objects.get(pk=pk)
#         # print('helo')
#     except:
#         return HttpResponse("Invalid")
#     if request.method=='GET':
#         s=studModelSerializer(demo)
#         return JsonResponse(s.data)
#     elif request.method=='PUT':
#         d=JSONParser().parse(request)
#         s=studModelSerializer(demo,data=d)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data)
#         else:
#             return JsonResponse(s.errors)       
#     elif request.method=='DELETE':
#         demo.delete()
#         return HttpResponse("Deleted")



#/-------------------------------------------------------------------------------------------------------\
#    ***************************************** API_VIEW  GET,POST ********************************
#\-------------------------------------------------------------------------------------------------------/



# @api_view(['GET','POST'])
# def fun1(req):
#     if req.method == 'GET':
#         d = stud.objects.all()
#         s = studModelSerializer(d, many=True)
#         return Response(s.data)

#     elif req.method == 'POST':
#         s = studModelSerializer(data=req.data)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse(s.errors, status=status.HTTP_400_BAD_REQUEST)




#/---------------------------------------------------------------------------------------------------------\
#   ***************************************** API_VIEW  GET,PUT,DELETE ********************************
#\---------------------------------------------------------------------------------------------------------/


# @api_view(['GET','PUT','DELETE'])
# def fun1(req,pk):
#     try:
#         demo=stud.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if req.method == 'GET':
#         s = studModelSerializer(demo)
#         return Response(s.data)
#     elif req.method == 'PUT':
#         s = studModelSerializer(demo,data=req.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif req.method == 'DELETE':
#         demo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# /-------------------------------------------------------------------------------------------\
#     **************************************  API_VIEW CLASS  *****************************
# \-------------------------------------------------------------------------------------------/

class fun1(APIView):
    def get(self,request):
       demo=stud.objects.all()
       s=studModelSerializer(demo,many=True)
       return Response(s.data)
    def post(self,request):
        s=studModelSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
