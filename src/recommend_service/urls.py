"""
URL configuration for recommend_service project.

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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from rest_framework import routers

from .views import UnitViewSet, RecommendationViewSet, UnitCreateView, RecommendationCreateView

router = routers.DefaultRouter()
router.register('units', UnitViewSet)
router.register('recommendations', RecommendationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login_form.html'), name='login'),
    path('unit/create/', UnitCreateView.as_view(), name='unit_create'),
    path('unit/<int:unit_id>/recommendation/create/', RecommendationCreateView.as_view(), name='recommendation_create'),
    path('api/', include(router.urls)),
]

if settings.ENV.upper() == 'DEV':
    urlpatterns = [path('dev/', include(urlpatterns))]
