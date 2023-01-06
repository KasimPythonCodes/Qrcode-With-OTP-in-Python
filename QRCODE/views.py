from django.shortcuts import render
import random
import qrcode
# Create your views here.

otp=0

def openLoginPage(request):
    return render(request , "login.html")


def validateuser(request):
    username=request.POST.get("t1")
    password=request.POST.get("t2")

    if username=="kasim" and password=="saifi":
         # create QRCODE
         rno=random.randint(10000, 99999)
         global otp
         otp = rno
         im=qrcode.make("OTP IS"+str(rno))
         im.save(r"QRCODE/static/qrimages/kasim.jpg")
         return render(request, "qrcode_page.html")
    else:
      return render(request, "login.html" ,{"message":"Invalid user"})



def validateOTP(request):  
    user_otp=request.POST.get("otp")
    if user_otp == str(otp):
        #open Wellcome
        return render(request , "welcome.html")
    else:
        return render(request , "login.html" ,{"message":"Invalid OTP"} )    
