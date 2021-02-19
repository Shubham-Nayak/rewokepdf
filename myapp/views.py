from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import *
from datetime import datetime,date,timedelta
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login
import datetime
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.core.files.storage import FileSystemStorage

def index(request):
   settings=Tbloptions.objects.all().first()

   if request.user.is_authenticated:

        banner=Tblcommonmasters.objects.filter(type='banner')
        try:
          subscriptions=Tblsubscription.objects.all()
        except Tblsubscription.DoesNotExist:
          subscriptions = None

        try:
          userdetails=Tbluserdetails.objects.get(userid=request.user.id)
        except Tbluserdetails.DoesNotExist:
          userdetails = None

        allprod={'banner':banner,'subscriptions':subscriptions,'userdetails':userdetails,'settings':settings}
        return render(request,'myapp/index.html',allprod)
   else:
        return render(request,'myapp/login.html')

def history(request):
   settings=Tbloptions.objects.all().first()

   if request.user.is_authenticated:
        history=Userpdfs.objects.all()
        allprod={'history':history,'settings':settings}
        return render(request,'myapp/history.html',allprod)
   else:
        return render(request,'myapp/login.html')


def signup(request):
    if request.method=="POST":
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,"myapp/login.html",{'error':'user alrady taken'})
            except Exception:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['pass1'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'])
                user.save()

                return render (request,'myapp/login.html',{'error':'signup sucessfull please login'})
                
        else:
            return render(request,"myapp/login.html",{'error':'password not match'})
    else:
        return render(request,"myapp/login.html")

   
def login(request):
 
    if request.method=="POST":
         if request.POST['username']!="" and request.POST['pass']!="":

                         user=auth.authenticate(username=request.POST['username'],password=request.POST['pass'])
                         if user is not None:
                              auth.login(request,user)
                              data = {'status': True,'data': 'Finland',    'message': 'Login Successfull','http_redirect':'/'}
                              return JsonResponse(data)
                         else:
                              data = {'status': False,'data': 'Finland',    'message': 'username and password was incorrect'}
                              return JsonResponse(data)
         else:
               data = {'status': False,'data': 'Finland',    'message': 'username and password is required'}
               return JsonResponse(data)
    else:
        data = {'status': False,'data': 'Finland',    'message': 'username and password was incorrect'}
        return JsonResponse(data)


def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return render(request,'myapp/login.html')


def buysubscription(request):
    settings=Tbluserdetails.objects.all().first()
    if request.method=="POST":
            try:
                 Tbluserdetails.objects.get(orderid=request.POST['orderid'])
                 messages.success(request, 'You alredy Have This Subscription')

                 return HttpResponseRedirect('/')
            except Exception:
                 orderid=request.POST['razorpay_order_id']
                 purchasedate = datetime.datetime.today()
                 expiredate = purchasedate + datetime.timedelta(days=int(request.POST['validity']))
                 user=User.objects.get(id=request.user.id)
                 subscription=Tblsubscription.objects.get(id=request.POST['subscription_id'])
                 paymentid=request.POST['razorpay_payment_id']
                 subscription=Tbluserdetails.objects.create(userid=user,subscription=subscription,purchasedate=purchasedate,expiredate=expiredate,orderid=orderid,paymentid=paymentid)
                 subscription.save()

                 messages.success(request, 'Your Subscription Is Activated')

                 return HttpResponseRedirect('/')
    else:
        return render(request,"myapp/index.html")


def checkout(request,myid):
     settings=Tbloptions.objects.all().first()
     subscriptions=Tblsubscription.objects.get(id=myid)
     amount= int(subscriptions.price)*int(100)
     client=razorpay.Client(auth=("rzp_test_UgBzAXaVEXTtT0","tbxfYBpMpPx6l0s3VNOzs8CW"))
     payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
     allprod={'payment':payment,'subscriptions':subscriptions,'settings':settings}
     return render(request,'myapp/checkout.html',allprod)




def savepdf(request):
     
     if request.method=="POST":
          if request.FILES['file']:
                        myfile = request.FILES['file']
                        user=User.objects.get(id=request.user.id)
                        pdf=Userpdfs.objects.create(userid=user,files=myfile,filename=myfile.name,filesize=myfile.size)
                        data = {'status': True,'data': 'Sucess',    'message': 'File Converted'}
                        return JsonResponse(data)
          else:
               data = {'status': False,'data': 'Denger',    'message': 'file required'}
               return JsonResponse(data)
     else:
        data = {'status': False,'data': 'Finland',    'message': 'something is wrong'}
        return JsonResponse(data)