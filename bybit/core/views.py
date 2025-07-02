from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().get(request, *args, **kwargs)

class CustomLogoutView(LogoutView):
    next_page = '/login/'  # Explicitly set redirect