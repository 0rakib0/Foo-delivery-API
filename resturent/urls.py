from django.urls import path, include

from . import views


urlpatterns = [
    path('menus/<resturent_id>/', views.MenusList, name="menus"),
    path('category/<resturent_id>/', views.CategoryList, name='category')
]