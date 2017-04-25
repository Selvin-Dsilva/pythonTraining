from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^test/',views.welcome),
    url(r'^training/',views.train_view),
]
