from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('login_redirect/', views.login_redirect_view, name='login_redirect'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]