"""
URL configuration for Hola_mundo project.

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
from django.urls import path
from tutorial.views import mostrar_acerca  # Reemplaza 'tutorial' por el nombre de tu app si es diferente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_acerca, name='inicio'),      # Para entrar directo desde http://127.0.0.1:8000/
    path('acerca', mostrar_acerca, name='acerca'), # Para entrar desde http://127.0.0.1:8000/acerca
]

