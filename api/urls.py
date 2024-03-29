from django.urls import  path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name = 'user-registration'),
    path('user-login/', views.user_login, name = 'user-login')
]
