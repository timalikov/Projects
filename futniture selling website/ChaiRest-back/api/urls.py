"""
URL configuration for ChaiRest project.

The urlpatterns list routes URLs to views. For more information please see:
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
from api import urls
from api.views import *
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import CustomTokenObtainPairView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_info/', user_info, name='user_info'),
    path('category/', CategoryListView.as_view(), name='category-list' ),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-details'),
    path('category/<int:id>/furniture/', CategoryFurnitureList.as_view(), name='furniture-list'),
    path('furniture/', FurnitureListView.as_view(), name='furniture-details'),
    path('furniture/<int:id>', FurnitureDetailView.as_view(), name='furniture-details'),
    path('order/<int:id>', create_order),
    path('auth/register/', RegisterView.as_view(), name='register'),
    # path('auth/login/', TokenObtainPairView.as_view(), name='jwt-obtain-token'),
    # path('auth/refresh/', TokenRefreshView.as_view(), name='jwt-refresh-token'),
    # path('auth/verify/', TokenVerifyView.as_view(), name='jwt-verify-token'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),

]