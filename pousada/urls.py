"""pousada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiRoot.as_view()),
    path('quarto/', QuartoList.as_view(), name=QuartoList.name),
    path('quarto/<int:pk>/', QuartoDetail.as_view(), name=QuartoDetail.name),
    path('reserva/', ReservaList.as_view(), name=ReservaList.name),
    path('reserva/<int:pk>/', ReservaDetail.as_view(), name=ReservaDetail.name),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
