from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render , redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from Account_Module.models import User
from UserPanel_Module.forms import EditProfileModelForm , ChangePasswordForm


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

class ChangePassword(View):
    def get(self, request:HttpRequest):
        context = {
            'form': ChangePasswordForm
        }
        return render(request, 'UserPanel_Module/ChangePassword.html', context)
    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = GetCurrentUser(request)
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('password', 'کلمه عبور وارد شده اشتباه میباشد')


        context = {
            'form': form
        }
        return render(request , 'UserPanel_Module/ChangePassword.html', context)
def UserPanelMenuComponent(request: HttpRequest):
    current_user = GetCurrentUser(request)
    context = {
        'current_user': current_user
    }
    return render(request, 'UserPanel_Module/components/UserSidebar.html', context)