from django import forms
from Account_Module.models import User

class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'about_user']

        widgets = {
            'first_name': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'نام'
            }),
            'last_name': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'نام خانوادگی'
            }),
            'avatar': forms.FileInput(attrs = {
                'class': 'form-control',
            }),
            'address': forms.Textarea(attrs = {
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'آدرس'
            }),
            'about_user': forms.Textarea(attrs = {
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'آدرس'
            })
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'تصویر پروفایل',
            'address': 'آدرس',
            'about_user': 'درباره شخص'
        }

        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خواندگی را وارد کنید'
            },
            'email': {
                'required': 'لطفا ایمیل را وارد کنید'
            },
            'title': {
                'required': 'لطفا عنوان را وارد کنید'
            },
            'message': {
                'required': 'لطفا متن پیام را وارد کنید'
            },
        }

        # fields = '__all__'
        # exclude = ['response'] will show all except response
