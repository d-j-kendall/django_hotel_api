from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Customer
from api.serializers import CustomerSerializers


@api_view(['GET', 'POST'])
def create_user(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Customer.objects.all()
        serializer = CustomerSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializers(request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save(request.data)
            
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
