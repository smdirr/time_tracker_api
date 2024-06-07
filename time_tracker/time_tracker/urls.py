"""
URL configuration for time_tracker project.

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
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from person.views import PersonListCreate, PersonDetail, register
from time_logging.views import TimeEntryViewSet, ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register(r"project", ProjectViewSet)
router.register(r"task", TaskViewSet)
router.register(r"time-entries", TimeEntryViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/v1/register/", register, name="user_register"),
    path("api/v1/person/", PersonListCreate.as_view(), name="person-list-create"),
    path("api/v1/person/<int:pk>/", PersonDetail.as_view(), name="person-detail"),
]
