from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from .models import Cust
import datetime


# Create your views here.



def cust_detail(request):
    if request.method=="POST":
        data=request.POST
        data_update= Cust(first_name=data['first_name'],last_name=data['last_name'],addrline1=data['addrl1'],addrline2=data['addrl2'],city=data['city'],state=data['state'],zip=data['zip'],email=data['email'],area_code=data['area'],phone=data['phone'])
        data_update.save()
        data_cust = Cust.objects.all()
        context = {
            'data_cust': data_cust
        }
        return render(request, 'django_assign/display_customer_details.html',context)
    else:
        context = {
        }
        return render(request,'django_assign/customer_details.html',context)

def cust_display(request):
    data_cust=Cust.objects.all()
    context = {
        'data_cust':data_cust
    }
    return render(request,'django_assign/display_customer_details.html',context)