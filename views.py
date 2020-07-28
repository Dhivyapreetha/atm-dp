from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import user,deposit,withdraw
from .serializers import userSerializer,depositSerializer,withdrawSerializer
from rest_framework.response import Response

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all().order_by('-id')
    serializer_class=AssetSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = userSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
            
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete() 
class depositViewSet(viewsets.ModelViewSet):
    queryset = deposit.objects.all().order_by('-id')
    serializer_class=AssetSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = depositSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
            
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete() 

class withdrawViewSet(viewsets.ModelViewSet):
    queryset = withdraw.objects.all().order_by('-id')
    serializer_class=AssetSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = withdrawSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
            
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete() 
