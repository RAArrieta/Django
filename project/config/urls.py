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
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include("cliente.urls")),
    path('producto/', include("producto.urls")),
    # path('cliente/', )
    # path("saludo/", views.saludo),
    # path("nombre/<apellido>/<nombre>",views.con_parametros),
    # path("template_prueba/", views.probando_template),
    # path("template_render/", views.template_render),
    # path("template_render_parametros", views.template_render_parametros),
    # path("ver_personas/", views.ver_personas)
]
