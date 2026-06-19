from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact , name="contact"),
    path('career', views.career , name="career"),
    path('sign/', views.sign, name="sign"),
    path('job/', views.job, name="job"),
    path('postjob/', views.postjob, name="postjob"),
    path('apply/', views.apply, name="apply")

    

]

