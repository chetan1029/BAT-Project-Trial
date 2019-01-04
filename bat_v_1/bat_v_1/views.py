from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(TemplateView):
    template_name = "index.html"

class TestPage(TemplateView):
    template_name = "test.html"

class DashboardPage(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = "dashboard"
        context['active_submenu'] = "basic"
        return context

class LogoutPage(TemplateView):
    template_name = "logout.html"
