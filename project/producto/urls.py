"""
URL configuration for config project.

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

from django.urls import path
from . import views


app_name = "producto"

urlpatterns = [
    path("", views.home, name="home"),
    path("productocategoria/create/", views.productocategoria_create,
         name="productocategoria_create"),
    path("instrumentoscuerdas/create/", views.instrumentos_de_cuerdas,
         name="instrumentos_de_cuerdas"),
    path("instrumentosaire/create/", views.instrumentos_de_aire,
         name="instrumentos_de_aire"),
    # path("productocategoria/create/", views.productocategoria_create,
    #      name="productocategoria_create"),
    # path("instrumentoscuerdas/create/", views.instrumentos_de_cuerdas,
    #      name="instrumentos_de_cuerdas"),
]
