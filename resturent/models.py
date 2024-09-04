from django.db import models
from users.models import User

# Create your models here.


class Resturent(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_restaurants')
    employees = models.ManyToManyField(User, related_name='employed_restaurants')
    location = models.CharField(max_length=255)  
    
    def __str__(self) -> str:
        return self.name
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=160)
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.name
    
    
class MenuItem(models.Model):
    name = models.CharField(max_length=260)
    description = models.TextField()
    print = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item')
    resurent = models.ForeignKey(Resturent, on_delete=models.CASCADE, related_name='resturent')
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Modifier(models.Model):
    name = models.CharField(max_length=260)
    aditional_price = models.IntegerField()
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='items')
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Order(models.Model):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quintity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=[('pending', 'pending'), ('complate','complate')])
    payment_method = models.CharField(max_length=20, choices=[('card', 'Card'), ('cash', 'Cash')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.quintity} X {self.menu_item.name}"
    

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=20, choices=[('card', 'Card'), ('cash', 'Cash')])
    payment_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Payment of {self.order.id}"
