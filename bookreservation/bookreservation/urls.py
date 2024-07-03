"""bookreservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from reservation import views, models
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('aboutus/', views.aboutus, name='aboutus'),
    path('studentinfo/', views.studentinfo, name='studentinfo'),
    path('bookinfo/', views.bookinfo, name='bookinfo'),
    path('login/', LoginView.as_view(template_name='reservation/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('bookreservation/', views.bookreservation, name="reservation"),
    path('savereservation', views.savereservation, name='savereservation'),
    path('dashboard/', views.chartdata, name='dashboard')
]
