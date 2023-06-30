from . import views
from django.urls import path

urlpatterns = [
    path("api/execute", views.ExecuteCode.as_view(), name="execute code")
]