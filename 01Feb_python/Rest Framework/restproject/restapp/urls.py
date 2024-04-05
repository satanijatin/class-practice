"""
URL configuration for restproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path,include
from .views import *

urlpatterns = [
 
    path('students/',StudentAPI.as_view()),
    path('products/',ProductAPI.as_view()),
    path('category/',CategoryAPI.as_view()),
    path("register/",RregisterUser.as_view()),    
    path('author/',AuthorAPI.as_view()),
    path('publisher/',PublisherAPI.as_view()),
    path("book/",BookAPI.as_view()),
    path('country/',CountryAPI.as_view()),
    path('state/',StateAPI.as_view()),
    path("city/",CityAPI.as_view()),
     path("area/",AreaAPI.as_view())
]
