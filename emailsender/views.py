from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .settings import EMAIL_HOST_USER

def show(request):
    return render(request,'index.html')

def sendEmail(request):
    context={}
    mail=request.POST.get("email")
    subject='sample testing mail'
    message='if you receive this mail you are very lucky'
    try:
        send_mail(subject,message,EMAIL_HOST_USER,[mail],fail_silently=False)
        messages.success(request,"email is sent to your email address")
        return  render(request,'index.html')
    except TypeError:
        return HttpResponse(TypeError.message)
