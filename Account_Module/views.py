from django.shortcuts import render , redirect
from django.views import View
from Account_Module.forms import RegisterForm


# Create your views here.

class RegisterView(View):
    def get(self , request ):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'Account_Module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            return redirect('/')

        context = {
            'register_form': register_form
        }
        return render(request, 'Account_Module/register.html', context)
