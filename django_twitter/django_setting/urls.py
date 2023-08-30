from django.urls import path
from . import views


urlpatterns = [
    path('settings/', views.setting, name='setting'),
    path('change_username/',views.change_username, name='change_username'),
    path('change_email/', views.change_email, name='change_email'),
    path('change_mobile-number/', views.change_mobile_number, name='change_mobile_number'),
    path('change_password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
]
