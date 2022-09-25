from django.urls import path,include
from csm_app1 import views


#include all the views of the csm_app1 which uses HTML pages 
urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup,name='signup'),
    path('form/',views.form, name='form'),
    path('about-us/',views.aboutus, name='about-us'),
    path('homepage/',views.homepage, name='homepage'),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    path('bookdetails/',views.bookdetails,name='bookdetails'),
    path('popup/',views.popup,name='popup'),
    
]
