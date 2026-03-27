"""
URL configuration for DjangoProject_Nhom05 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from DjangoProject_Nhom05 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/collagen/', views.service_detail, name='service_detail'),
    path('account/', views.account, name='account'),
    path('consult/', views.consult, name='consult'),
    path('reviews/', views.reviews, name='reviews'),
    path('reviews/service-detail/', views.review_service_detail, name='review_service_detail'),
    path('reviews/write/', views.review_write, name='review_write'),
    path('reviews/detail/', views.review_detail, name='review_detail'),
    path('reviews/deleted/', views.review_delete_success, name='review_delete_success'),
    path('account/profile/', views.account_profile, name='account_profile'),
    path('account/history/', views.account_history, name='account_history'),
    path('account/points/', views.account_points, name='account_points'),
    path('booking/service/', views.booking_service, name='booking_service'),
    path('booking/package/', views.booking_package, name='booking_package'),
    path('booking/time/', views.booking_time, name='booking_time'),
    path('booking/confirm/', views.booking_confirm, name='booking_confirm'),
    path('appointments/', views.appointments, name='appointments'),
]
