from django.contrib import admin
from django.urls import path
from calories import views
from .views import home,add_user_entry,add_food,select_food,add_user_entry,delete_consume
urlpatterns = [
    path('',home,name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('addentry/',add_user_entry,name='add_user_entry'),
    path('add_food/', add_food, name='add_food'),
    path('select_food/', select_food, name='select_food'),
    path('add_user_entry/',add_user_entry,name='add_user_entry'),
    path('delete/<int:id>/', delete_consume, name="delete"),
    # path('<str:name>/',food_delete,name='food_delete'),
]
