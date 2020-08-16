from django.shortcuts import render
from .serialzier import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self,request,pk=None):
        try:
            user = self.queryset.get(pk=pk)
            serializer = self.serializer_class(user)
            data = serializer.data
            return Response({'message1':"your response have been taken","message2":"we are procceding to your response","data":data})
        except:
            return Response({"message":"Uses not defined"})

    def destroy(self, request, pk=None):
        try:
            user_obj = self.queryset.get(pk=pk)
            user_obj.delete()
            return Response({'message':'User is deleted successfully'})
        except:
            return Response({'message':'User is not available'})

    def update(self, request, pk=None):
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.serializer_class(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data=serialzier.data
            return Response({'message1':"your response have been taken","message2":"we are procceding to your response","data":data})
        except:
            return Response({"Uses not defined"})