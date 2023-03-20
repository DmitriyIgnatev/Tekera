from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm)
from .models import Application
from django.forms import ModelForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

        class Meta:
            fields = ('password1', 'password2')


class Application_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Application
        fields = ('name', 'phone')
        labels = {
            Application.name.field.name: 'Ваше имя'
        }
