from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

def add_form_control_to_fields(form):
    for visible in form.visible_fields():
        visible.field.widget.attrs['class'] = 'form-control'

class RegisterForm(forms.Form):
    email = forms.EmailField(
        label = 'ایمیل' ,
        widget = forms.EmailInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
            validators.EmailValidator
        ]
    )

    password = forms.CharField(
        label = 'کلمه عبور' ,
        widget = forms.PasswordInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
        ]
    )
    confirm_password = forms.CharField(
        label = 'تکرار کلمه عبور' ,
        widget = forms.PasswordInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
        ]
    )

    def __init__( self , *args , **kwargs ):
        super(RegisterForm , self).__init__(*args , **kwargs)
        add_form_control_to_fields(self)

    def clean_confirm_password( self ):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        raise ValidationError('کلمه عبور با تکرار ان یکسان نیست')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label = 'ایمیل' ,
        widget = forms.EmailInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
            validators.EmailValidator
        ]
    )

    password = forms.CharField(
        label = 'کلمه عبور' ,
        widget = forms.PasswordInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
        ]
    )

    def __init__( self , *args , **kwargs ):
        super(LoginForm , self).__init__(*args , **kwargs)
        add_form_control_to_fields(self)
# ! Use modelForm when you have fully customizable model because it will read validations and stuffs from model

class Forget_Password_Form(forms.Form):
    email = forms.EmailField(
        label = 'ایمیل',
        widget = forms.EmailInput(),
        required = True,
        validators = [
            validators.MaxLengthValidator(100) ,
            validators.EmailValidator
        ]
    )

    def __init__( self , *args , **kwargs ):
        super(Forget_Password_Form , self).__init__(*args , **kwargs)
        add_form_control_to_fields(self)


class Reset_Password_Form(forms.Form):
    password = forms.CharField(
        label = 'کلمه عبور' ,
        widget = forms.PasswordInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
        ]
    )
    confirm_password = forms.CharField(
        label = 'تکرار کلمه عبور' ,
        widget = forms.PasswordInput() ,
        validators = [
            validators.MaxLengthValidator(100) ,
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        raise ValidationError('کلمه عبور با تکرار ان یکسان نیست')
    def __init__( self , *args , **kwargs ):
        super(Reset_Password_Form , self).__init__(*args , **kwargs)
        add_form_control_to_fields(self)

