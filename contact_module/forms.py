from django import forms

from .models import ContactUs


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

    email = forms.EmailField(label = 'ایمیل' , required = False , widget = forms.EmailInput(attrs = {
        'class': 'form-control',
        'placeholder': 'ایمیل '
    })
                             )
    title = forms.CharField(label = 'عنوان',
            widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'عنوان'
        }))

    message = forms.CharField(label = 'متن پیام',widget = forms.Textarea(attrs = {
        'class': 'form-control',
        'placeholder': 'متن پیام',
        'rows': '5',
        'id': 'message'
    }))

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['response'] will show all except response