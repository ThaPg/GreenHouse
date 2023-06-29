from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import graph1

urlpatterns = [
    # path("", views.main, name="main"),
    path("register", views.register_request, name="register"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    # path("graph1", graph1.as_view(), name="graph1"),
]
