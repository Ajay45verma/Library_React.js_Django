from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Demo, User
from .serializers import *

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
def Demo_test(request):
    permission_classes = (AllowAny)
    if request.method == 'GET':
        data = Demo.objects.all()

        serializer = DemSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        #x=request.POST.get("userData")
        x=request.data
        print(x["mail"])
        serializer = DemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            dat={
                'msg':' Data Created'
            }
            #serializer.create(serializer.data)
            return Response(dat,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def UserVi(request):
    if request.method=="POST":
        fdata=request.data
       # print(fdata['fname'], fdata['lname'])
        fname=fdata['fname']
        lname=fdata['lname']
        email=fdata['email']
        password=fdata['password']
        cpassword=fdata['cpassword']
        ud={
            'fname':fname,
            'lname':lname,
            'email':email,
            'password':password,
        }
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            dat={
                'msg':' Data Created'
            }
            #serializer.create(serializer.data)
            return Response(dat,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    

