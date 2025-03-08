from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NationalIDSerializer
from .utils import validate_api_key

class NationalIDValidatorView(APIView):

    def post(self, request, *args, **kwargs):
        api_key_validation_response = validate_api_key(request)
        if api_key_validation_response:
            return api_key_validation_response 
        serializer = NationalIDSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
