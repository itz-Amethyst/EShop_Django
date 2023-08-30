from django import forms


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
    subject = forms.CharField(label = 'عنوان',
            widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'عنوان'
        }))
    email = forms.EmailField(label = 'ایمیل', required = False, widget = forms.EmailInput(attrs = {
            'class': 'form-control',
            'placeholder': 'ایمیل '
        })
    )
    text = forms.CharField(label = 'متن پیام',widget = forms.Textarea(attrs = {
        'class': 'form-control',
        'placeholder': 'متن پیام',
        'rows': '5',
        'id': 'message'
    }))