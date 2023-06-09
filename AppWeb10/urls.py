"""AppWeb10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from signup.views import signaction
from login.views import loginaction

# Otro forma
# from signup import views as views_signup
# from login import views as views_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signaction),
    path('login/' , loginaction),
    # path('login/' , include("login.urls")),
    # path('signup/', include("signup.urls")),

    # Otra forma
    # path('admin', views_signup.signaction),
    # path('admin', views_login.loginaction),
]
