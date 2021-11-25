from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('accounts/' , include('django.contrib.auth.urls')),
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),



]
