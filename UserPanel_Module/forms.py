from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from Account_Module.forms import add_form_control_to_fields
from Account_Module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'avatar' , 'address' , 'about_user']

        widgets = {
            'first_name': forms.TextInput(attrs = {
                'class': 'form-control' ,
                'placeholder': 'نام'
            }) ,
            'last_name': forms.TextInput(attrs = {
                'class': 'form-control' ,
                'placeholder': 'نام خانوادگی'
            }) ,
            'avatar': forms.FileInput(attrs = {
                'class': 'form-control' ,
            }) ,
            'address': forms.Textarea(attrs = {
                'class': 'form-control' ,
                'rows': 3 ,
                'placeholder': 'آدرس'
            }) ,
            'about_user': forms.Textarea(attrs = {
                'class': 'form-control' ,
                'rows': 5 ,
                'placeholder': 'آدرس'
            })
        }

        labels = {
            'first_name': 'نام' ,
            'last_name': 'نام خانوادگی' ,
            'avatar': 'تصویر پروفایل' ,
            'address': 'آدرس' ,
            'about_user': 'درباره شخص'
        }

        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خواندگی را وارد کنید'
            } ,
            'email': {
                'required': 'لطفا ایمیل را وارد کنید'
            } ,
            'title': {
                'required': 'لطفا عنوان را وارد کنید'
            } ,
            'message': {
                'required': 'لطفا متن پیام را وارد کنید'
            } ,
        }

        # fields = '__all__'
        # exclude = ['response'] will show all except response


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label = 'کلمه عبور فعلی' ,
        widget = forms.PasswordInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
        ]
    )

    password = forms.CharField(
        label = 'کلمه عبور' ,
        widget = forms.PasswordInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
        ]
    )
    confirm_new_password = forms.CharField(
        label = 'تکرار کلمه عبور جدید' ,
        widget = forms.PasswordInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
        ]
    )

    def clean_confirm_new_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_new_password')

        if password == confirm_password:
            return confirm_password
        raise ValidationError('کلمه عبور با تکرار ان یکسان نیست')


    def __init__( self , *args , **kwargs ):
        super(ChangePasswordForm , self).__init__(*args , **kwargs)
        add_form_control_to_fields(self)
