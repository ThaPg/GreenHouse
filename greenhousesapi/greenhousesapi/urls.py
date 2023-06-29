"""
URL configuration for greenhousesapi project.

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
from django.urls import path, include
from greenhouses import views

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("chaining/", include("smart_selects.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns += [
    path("greenhouses/", include("greenhouses.urls")),
    path("contact/", views.contact),
    path("company/", views.company),
    path("partner/", views.partner),
    path("graph1/", views.graph1),
]
