from django.urls import path
from . import views

urlpatterns = [
    path('validate_nid/', views.NationalIDValidatorView.as_view(), name='validate_national_id'),
]