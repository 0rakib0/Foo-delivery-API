from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework import status
from .models import User
from rest_framework.authtoken.models import Token

# Create your views here.

class testAPI(APIView):
    
    def get(self, request, format=None):
        return Response ({"Name":"Rakibul Hasan"})
    
class Register(APIView):
    
    def post(self, request, format=None):
        userData = UserSerializer(data=request.data) # get user data by post request
        if userData.is_valid(): # check this data valid or not
            userData.save()  # if data is valid then save data 
            user = User.objects.get(username=userData.data['username'])
            token_obj, other = Token.objects.get_or_create(user=user)
            return Response({'message':'user successfully register', 'token':str(token_obj)}, status=status.HTTP_201_CREATED)
        
        else:
            return Response({'message':'Something wrong'}, userData.errors)



