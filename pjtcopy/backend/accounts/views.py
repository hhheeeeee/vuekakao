from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from rest_framework import status
from .models import User

class CustomUser(User):
    username_validator = ASCIIUsernameValidator()

@api_view(['GET'])
def duplicateID(request, username):
    if request.method == 'GET':
        existing_user = User.objects.filter(username=username)
        if len(existing_user) != 0:
            return Response({'message':'fail'})
        else:
            return Response({'message':'ok'})
    
