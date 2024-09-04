from django.urls import path, include

from . import views


urlpatterns = [
    path('add-category/', views.AddCategory.as_view()),
    path('add-menu-item/', views.AddMenuItem.as_view()),
    path('add-modifier-item/', views.AddModifier.as_view()),
    path('order-place/', views.PlaceOrder.as_view()),
    path('receive-payment/', views.ReceivePayment.as_view()),
    path('menus/<resturent_id>/', views.MenusList, name="menus"),
    path('category/<resturent_id>/', views.CategoryList, name='category'),
    path('modifier/<item_id>/', views.ModifireList, name='modifi')
]