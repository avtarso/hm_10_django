from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users_main, name='users_main'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
