from django.urls import path
from . import views

urlpatterns = [
    path('', views.testAPI.as_view()),
    path('register/', views.Register.as_view()),
]