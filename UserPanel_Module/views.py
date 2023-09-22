from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from UserPanel_Module.forms import EditProfileModelForm


# Create your views here.

class UserPanelDashboardClass(TemplateView):
    template_name = 'UserPanel_Module/UserPanelDashboard.html'

class EditUserProfile(View):
    def get( self, request:HttpRequest ):
        edit_form = EditProfileModelForm
        context = {
            'form': edit_form
        }
        return render(request, 'UserPanel_Module/EditProfile.html', context)
    def post( self, request:HttpRequest ):
        return render(request, 'UserPanel_Module/EditProfile.html', {})
def UserPanelMenuComponent(request: HttpRequest):
    return render(request, 'UserPanel_Module/components/UserSidebar.html')