"""
URL configuration for AITool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home
from objectDetection.views import ObjectDetection
from carCounting.views import CarCounting
from peopleCounting.views import PeopleCounting
from complain.views import complain
from about.views import aboutUs
from contactUs.views import contactUs
from Feedback.views import feedback
from services.views import services


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('object_detection/',ObjectDetection,name='ObjectDetection'),
    path('PeopleCounting/',PeopleCounting,name='PeopleCounting'),
    path('CarCounting/',CarCounting,name='CarCounting'),
    path('contact-us/',contactUs,name='contactUs'),
    path('about-us/',aboutUs,name='aboutUs'),
    path('complain/',complain,name='complain'),
    path('feedback/',feedback,name='feedback'),
    path('services/',services,name='services'),
    
]
