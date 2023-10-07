from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator , MaxValueValidator

from Account_Module.models import User


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control' ,
            'placeholder': 'تکرار رمز عبور'
        }) ,
        label = 'تکرار رمز عبور'
    )

    class Meta:
        model = User
        fields = ['email' , 'password']
        widgets = {
            'email': forms.EmailInput(attrs = {
                'class': 'form-control' ,
                'placeholder': 'ایمیل' ,
            }) ,
            'password': forms.PasswordInput(attrs = {
                'class': 'form-control' ,
                'placeholder': 'رمز عبور'
            }) ,
        }
        labels = {
            'email': 'ایمیل' ,
            'password': 'رمز عبور' ,
        }

        error_messages = {
            'email': {
                'required': 'لطفا ایمیل را وارد کنید'
            } ,
            'password': {
                'required': 'لطفا رمز عبور را وارد کنید'
            } ,
            'confirm_password': {
                'required': 'لطفا تکرار رمز عبور را وارد کنید'
            } ,
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        raise ValidationError('تکرار کلمه عبور اشتباه است')

        # fields = '__all__'
        # exclude = ['response'] will show all except response
