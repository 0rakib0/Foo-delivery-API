from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MenuSerializer, CategorySerializer
from .models import MenuItem, Category
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def MenusList(request, resturent_id):
    
    try:
        int(resturent_id)
    except ValueError:
        return Response({"message": "Invalid restaurant ID. Please provide a numerical ID."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        menus = MenuItem.objects.filter(resurent=resturent_id)
    except MenuItem.DoesNotExist:
        return Response({"message":"Menu Item Does Not Exist!"})
    if(not menus):
        return Response({"message":"No Manu Item Found"})
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CategoryList(resquest, resturent_id):
    
    try:
        int(resturent_id)
    except ValueError:
        return Response({"message": "Invalid restaurant ID. Please provide a numerical ID."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        category = Category.objects.filter(resturent=resturent_id)
    except Category.DoesNotExist:
        return Response({"message":"Category Does Not Exist"})   
         
    if(not category):
        return Response({"message":"No Category Found"})
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

