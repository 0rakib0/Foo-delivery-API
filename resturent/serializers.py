from rest_framework import serializers
from .models import MenuItem, Category, Modifier, Order



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = '__all__'
        
        
class OrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'