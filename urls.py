from django .contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('', views.home, name='home'),
     path("about/",views.about,name='about'),
     path("login/",views.user_login,name='login'),
     path("res/",views.res,name='res'),
     path("contact/",views.contact,name='contact'),
     path("atc/",views.atc,name='atc'),
     path("forgetpass/",views.forgetpass,name='forgetpass'),
     path("payment/",views.payment,name='payment'),
     path("UPI/",views.UPI,name='UPI'),
     path("card/",views.card,name='card'),
     path("success/",views.success,name='success'),
]

