"""
URL configuration for sistemaVentas project.

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
from django.urls import path
from aplicacion1.views import LandingPage, Usuarios, FormularioUsuariosView, PaginaRestringidaView
from django.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='inicio'),
    path("usuarios/", Usuarios.as_view(), name="usuarios"),
    path("formulariousuarios/", FormularioUsuariosView.as_view(), name="registro"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("paginarestringida", login_required(PaginaRestringidaView.as_view()), name="paginaRestringida"),
]
