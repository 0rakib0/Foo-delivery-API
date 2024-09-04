from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MenuSerializer, CategorySerializer, ModifierSerializer
from .models import MenuItem, Category, Modifier
from rest_framework import status
# Create your views here.

class AddCategory(APIView):
    
    def post(self, request, format=None):
        category_data = CategorySerializer(data=request.data)
        if(category_data.is_valid()):
            category_data.save()
            return Response({"message":"category Sccessfully added."}, status=status.HTTP_201_CREATED)
    
        return Response(category_data.errors, status=status.HTTP_400_BAD_REQUEST)



class AddMenuItem(APIView):
    
    def post(self, request, format=None):
        menuItem_data = MenuSerializer(data=request.data)
        if(menuItem_data.is_valid()):
            menuItem_data.save()
            return Response({"message":"Menu Item succcessfully created"}, status=status.HTTP_201_CREATED)
        return Response(menuItem_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddModifier(APIView):
    def post(self, request, format=None):
        modifire_data = ModifierSerializer(data=request.data)
        
        if(modifire_data.is_valid()):
            modifire_data.save()
            return Response({"message":"Modifier menu item successfully added"}, status=status.HTTP_201_CREATED)
        
        return Response(modifire_data.errors, status=status.HTTP_400_BAD_REQUEST)





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


@api_view(['GET'])

def ModifireList(request, item_id):
    
    try:
        int(item_id)
    except ValueError:
        return Response({"message": "Invalid Item ID. Please provide a numerical ID."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        modifire = Modifier.objects.filter(item=item_id)
    except Modifier.DoesNotExist:
        return Response({"message":"Modifier Does Not Exist"})
    
    serializer = ModifierSerializer(modifire, many=True)
    return Response(serializer.data)

