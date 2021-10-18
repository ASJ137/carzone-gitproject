from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path("login", views.login,name="login"),
    path("register", views.register,name="register"),
    path("logout", views.logout,name="logout"),
    path("dashboard", views.dashboard,name="dashboard"),
    #path("<int:id>",views.car_detail,name="car_detail"),
    #path("search",views.search,name="search"),
    #path("contact",views.contact,name="contact"),
]
