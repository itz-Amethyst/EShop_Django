from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from Account_Module.models import User
from UserPanel_Module.forms import EditProfileModelForm


# Create your views here.

def GetCurrentUser(request:HttpRequest):
    return User.objects.filter(id = request.user.id).first()

class UserPanelDashboardClass(TemplateView):
    template_name = 'UserPanel_Module/UserPanelDashboard.html'

class EditUserProfile(View):
    def get(self, request:HttpRequest):
        current_user = GetCurrentUser(request)
        edit_form = EditProfileModelForm(instance = current_user)
        context = {
            'form': edit_form,
        }
        return render(request, 'UserPanel_Module/EditProfile.html', context)
    def post(self, request:HttpRequest):
        current_user = GetCurrentUser(request)
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance = current_user)
        if edit_form.is_valid():
            edit_form.save(commit = True)
        context = {
            'form': edit_form
        }

        return render(request, 'UserPanel_Module/EditProfile.html', {})
def UserPanelMenuComponent(request: HttpRequest):
    current_user = GetCurrentUser(request)
    context = {
        'current_user': current_user
    }
    return render(request, 'UserPanel_Module/components/UserSidebar.html', context)