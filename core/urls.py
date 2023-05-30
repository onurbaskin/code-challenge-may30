from django.urls import path
from core.views import UserView, CompanyView, PermissionGroupView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('company/', CompanyView.as_view()),
    path('permission-group/', PermissionGroupView.as_view()),
]
