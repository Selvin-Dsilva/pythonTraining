from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^customer_details/',views.cust_detail),
    url(r'^customer_display/',views.cust_display),
]
