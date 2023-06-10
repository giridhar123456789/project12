from django.shortcuts import render
from django.views import View
import requests
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from project12.settings import EMAIL_HOST_USER
from emailandsmsapp.forms import RegForm
from .models import RegModel
# Create your views here.
class Home(View):
    def get(self,request):
        rf=RegForm()
        con_dic={'rf':rf}
        return render(request,'hom.html',context=con_dic)
class Reg(View):
    def post(self,request):
        otp=str(random.randint(10000000,99999999))
        print(otp)
        mobno=request.POST["Mobno"]
        emailid=request.POST["Email"]
        resp = requests.post('https://textbelt.com/text',{
            'phone': mobno,
            'message': otp,
            'key':'375e260a9696e4d932e50a47b69a603d4ab539aal1gYx0keKtpxM8da0dO0UfIqW'
        })
        print(resp.json())
        send_mail("otp for registration",otp,EMAIL_HOST_USER,[emailid],fail_silently=True)
        rf=RegForm(request.POST)
        if rf.is_valid():
            rf.save()
            return HttpResponse("reg success")