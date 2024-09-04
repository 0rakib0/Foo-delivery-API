from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('resturent.urls')),
    path('login/', views.obtain_auth_token) # auth token buildin routs for login and generet token
]
