# yatube_api/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.views.generic import TemplateView # Если используете для redoc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')), # Ваши основные эндпоинты API

    # Эндпоинты для JWT-аутентификации (simplejwt)
    # Они должны соответствовать путям, которые ищут тесты:
    # /api/v1/jwt/create/
    # /api/v1/jwt/refresh/
    # /api/v1/jwt/verify/
    path('api/v1/jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('api/v1/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('api/v1/jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),

    # Если используете redoc
    path('redoc/', TemplateView.as_view(template_name='redoc.html'), name='redoc'),
]
