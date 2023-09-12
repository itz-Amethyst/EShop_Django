from django.contrib.auth import login , logout
from django.http import Http404
from django.shortcuts import render , redirect
from django.urls import reverse
from django.views import View
from Account_Module.forms import RegisterForm , LoginForm , Forget_Password_Form , Reset_Password_Form
from Account_Module.models import User
from django.utils.crypto import get_random_string
from utils.email_service import send_email


# Create your views here.

class RegisterView(View):
    def get( self , request ):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request , 'Account_Module/register.html' , context)

    def post( self , request ):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact = user_email).exists()

            if user:
                register_form.add_error('email' , 'ایمل وارد شده تکراری میباشد')
            else:
                new_user = User(email = user_email , email_active_code = get_random_string(48) , is_active = False ,
                                username = user_email)
                new_user.set_password(user_password)
                new_user.save()

                print(register_form.cleaned_data)

                send_email('فعال سازی حساب کاربری' , new_user.email , {'user': new_user} , 'emails/activate_account.html')
                return redirect(reverse('login_page'))
            return redirect('/')

        context = {
            'register_form': register_form
        }
        return render(request , 'Account_Module/register.html' , context)


class LoginView(View):
    def get( self , request ):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request , 'Account_Module/login.html' , context)

    def post( self , request ):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get("email")
            user_password = login_form.cleaned_data.get("password")
            user: User = User.objects.filter(email__iexact = user_email).first()
            if user != None:
                if not user.is_active:
                    login_form.add_error('email' , 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request , user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email' , 'نام کاربری یا کلمه عبور اشتباه است')

            else:
                login_form.add_error('email' , 'نام کاربری یا کلمه عبور اشتباه است')
        context = {
            'login_form': login_form
        }

        return render(request , 'Account_Module/login.html' , context)


class ActivateAccountView(View):
    def get( self , request , email_active_code ):
        user: User = User.objects.filter(email_active_code__iexact = email_active_code).first()
        if user != None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(42)
                user.save()
                # Todo show success message
                return redirect(reverse('login_page'))
            else:
                pass
                # Todo show you account was activated
        raise Http404


class ForgetPasswordView(View):
    def get(self, request):
        forget_password_form = Forget_Password_Form

        return render(request , 'Account_Module/forget_password.html' , context = {
            'forget_password_form': forget_password_form
        })

    def post(self, request):

        forget_password_form = Forget_Password_Form(request.POST)
        if forget_password_form.is_valid():
            user_email = forget_password_form.cleaned_data.get("email")
            user: User = User.objects.filter(email__iexact = user_email).first()
            if user != None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forget_password.html')
                return redirect(reverse('home_page'))
            else:
                forget_password_form.add_error('email', 'کاربری با این ایمیل یافت نشد')
        return render(request, 'Account_Module/forget_password.html', context = {
            'forget_password_form': forget_password_form
        })


class ResetPasswordView(View):
    def get( self , request , active_code ):
        # Todo change this later to forget_password_code and create it in model
        user: User = User.objects.filter(email_active_code__iexact = active_code).first()

        if user == None:
            return redirect(reverse('login_page'))

        reset_password_form = Reset_Password_Form

        return render(request , 'Account_Module/reset_password.html' , context = {
            'reset_password_form': reset_password_form ,
            'user': user
        })

    def post( self , request , active_code ):
        reset_password_form = Reset_Password_Form(request.POST)
        user: User = User.objects.filter(email_active_code__iexact = active_code).first()
        if reset_password_form.is_valid():
            user_new_password = reset_password_form.cleaned_data.get('password')

            if user == None:
                return redirect(reverse('login_page'))

            user.set_password(user_new_password)
            user.email_active_code = get_random_string(42)
            # Doestn matter
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))


        return render(request , 'Account_Module/reset_password.html' , context = {
            'reset_password_form': reset_password_form ,
            'user': user
        })


class LogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect(reverse('home_page'))
