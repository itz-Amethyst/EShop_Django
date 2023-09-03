from django import forms

from .models import ContactUs


#! Another way but needed to get cleaned data in views and define everyone of fields !
class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label = "نام و نام خانوادگی",
        max_length = 50,
        error_messages = {
        'required': 'لطفا نام و نام خواندگی را وارد کنید',
        'max_lenght': 'نام و نام خانوادگی نمیتواند بیشتر از 50 کاراکتر باشد'
        },
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })

    )

    email = forms.EmailField(label = 'ایمیل' ,
        error_messages = {
            'required': 'لطفا ایمیل را وارد کنید' ,
            },
        widget = forms.EmailInput(attrs = {
        'class': 'form-control',
        'placeholder': 'ایمیل '
    })
                             )
    title = forms.CharField(label = 'عنوان',
            widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'عنوان'
        }))

    message = forms.CharField(label = 'متن پیام',
        error_messages = {
            'required': 'لطفا متن پیام را وارد کنید' ,
            },
        widget = forms.Textarea(attrs = {
        'class': 'form-control',
        'placeholder': 'متن پیام',
        'rows': '5',
        'id': 'message'
    }))

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'ایمیل '
            }),
            'title': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'عنوان'
            }),
            'message': forms.Textarea(attrs = {
                'class': 'form-control',
                'rows': 5,
                'id': 'message',
                'placeholder': 'متن پیام'
            })
        }

        labels = {
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'title': 'عنوان',
            'message': 'متن پیام'
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

class ProfileForm(forms.Form):
    user_image = forms.FileField()