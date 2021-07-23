from django.urls import path, include
from . import views 

urlpatterns = [
    path('todo_app/', views.todo_app ,name="todo_app"),
    path('', views.todo_app ,name="base"),
    path('register/', views.registerPage ,name="register"),
    path('login/', views.loginPage ,name="login"),
    
    path('logout/', views.logoutUser ,name="logout"),
    
]
