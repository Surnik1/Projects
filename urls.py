"""
URL configuration for idkproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,re_path,include
from idkapp import views
product_pat = [path('',views.article),path('<int:id>',views.id),path('<int:id>/top',views.top_id),
               path('top',views.top),path('top/views',views.most_readible)]
 

urlpatterns = [
    path('', include(product_pat)),
    path('theme/',views.theme),
    
]
#path(route,view,kwargs=None,name=None)
#re_path(route,view,kwargs=None,name=None)