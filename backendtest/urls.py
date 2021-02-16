from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoginView, name='login'), # path to login view
    path('homepage', views.HomepageView, name='homepage'), # path to homepage view
    path('api',views.APIView, name='api'),
]