from django.urls import path
from . import views

app_name = 'User'
urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
