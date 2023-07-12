from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/post', views.PostViewSet, basename='post')

urlpatterns = [
    path("", include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', views.RegisterUser.as_view(),name="create_user"),
    path("api/execute", views.ExecuteCode.as_view(), name="execute_code"),
     path('', include(router.urls)),
]