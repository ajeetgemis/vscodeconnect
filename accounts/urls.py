from django.contrib import admin
from django.urls import path,include
from .views import signin,signup,verify_otp,login_otp_verify,signout
urlpatterns = [
    path('',signup,name="signup"),
    path('signin',signin,name="signin"),
    path('verify_otp',verify_otp,name="verify_otp"),
    path('login_verify_otp',login_otp_verify,name="login_verify_otp"),
   # path('home',home,name="home"),
    path('logout',signout,name="logout"),

]