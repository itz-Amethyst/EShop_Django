from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label = "نام و نام خانوادگی", max_length = 50, error_messages = {
        'required': 'لطفا نام و نام خواندگی را وارد کنید'
    })
    subject = forms.CharField(label = 'عنوان')
    email = forms.EmailField(label = 'ایمیل' , required = False)
    text = forms.CharField(widget = forms.Textarea, label = 'متن پیام')