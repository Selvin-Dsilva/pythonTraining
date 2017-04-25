from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from .models import Blog


# Create your views here.

def welcome(request):
    data_blog=Blog.objects.all()
    name="selvin"
    template = loader.get_template('django_one/index.html')
    context = {
        'name': name,
        'data_blog':data_blog
    }
    return render(request,'django_one/index.html',context)
    #return HttpResponse(template.render(context, request))
    #return render_to_response('index.html',{'name':name})
    #return HttpResponse("Hello, world. You're at the polls index.")

def train_view(request):
    if request.method=="POST":
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        data=request.get("title")
    else:
        print("inside else")
        data_blog=Blog.objects.all()
        name="selvin"
        context = {
            'name': name,
            'data_blog':data_blog
        }
        return render(request,'django_one/train.html',context)