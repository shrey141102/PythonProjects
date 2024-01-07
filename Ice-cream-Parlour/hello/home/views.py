from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages
# Create your views here.
def index(request):
    #return HttpResponse('this is homepage')
    context={
        "variable":"Shubha is great"
    }
    messages.success(request,"this is a test message")
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
    #return HttpResponse('this is about page')

def services(request):
    return render(request,'services.html')
   #return HttpResponse('this is services page')

def contacts(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contacts= Contacts(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contacts.save()
        messages.success(request, "Your message has been sent!!!!")
    return render(request,'contacts.html')
    #return HttpResponse('this is contact page')  