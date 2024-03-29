"""dm_hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
import django.conf.urls as conf_urls
import django
import api.resources as apres
from api import views
import home.views
customer_resource = apres.CustomerResource()
reservation_resource = apres.ReservationResource()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(customer_resource.urls)),
    path('api/', include(reservation_resource.urls)),
    path('account/', include('django.contrib.auth.urls')),
    path('', home.views.index, name='index'),
    path('make_cust',home.views.create_cust, name='make_cust'),
    path('new_customer/', views.create_user),
    path('make_res/', home.views.make_reservation),
    path('check_reservation/', home.views.check_reservation)
    ]
