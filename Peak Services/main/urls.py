from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/add/', views.add_item, name='add_item'),
    path('inventory/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('inventory/update/<int:item_id>/', views.update_stock, name='update_stock'),

 ]