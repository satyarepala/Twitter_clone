from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('upload/', views.upload_post, name='upload_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]

