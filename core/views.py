from django.shortcuts import render
from core.models import User, Company, PermissionGroup
from core.serializers import UserSerializer, PermissionGroupSerializer, CompanySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CompanyView(APIView):
    
    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PermissionGroupView(APIView):
    
    def get(self, request, format=None):
        permission_groups = PermissionGroup.objects.all()
        serializer = PermissionGroupSerializer(permission_groups, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PermissionGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = UserSerializer(users, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)