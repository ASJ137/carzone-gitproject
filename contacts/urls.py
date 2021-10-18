from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("inquiry", views.inquiry,name="inquiry"),
    #path("<int:id>",views.car_detail,name="car_detail"),
    #path("search",views.search,name="search"),
    #path("contact",views.contact,name="contact"),
]
