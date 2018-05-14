from django.shortcuts import render
from django.http import HttpResponse
from wall import models
def index(request):
    message=models.message.objects.all()
    return render(request,'index.html',{'message':message})
# Create your views here.
def post_data(request):
   # message_date=request.POST.get('message_date')
    message_content=request.POST.get('message')
    models.message.objects.create(message_content=message_content)
    message=models.message.objects.all()
    return render(request,'index.html',{'message':message})
