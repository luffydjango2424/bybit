from django.urls import path
from .views import CustomLoginView, DashboardView, CustomLogoutView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),  # Root URL for dashboard
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Override default logout
]