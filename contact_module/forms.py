from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label = "نام و نام خانوادگی")
    subject = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)