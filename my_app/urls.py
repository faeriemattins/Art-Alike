
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='my_app-home'),
    path('login/', views.login, name='my_app-login'),
    path('signup/', views.signup, name='my_app-signup'),
]
