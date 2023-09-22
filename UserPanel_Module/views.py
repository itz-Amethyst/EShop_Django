from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class UserPanelDashboardClass(TemplateView):
    template_name = 'UserPanel_Module/UserPanelDashboard.html'