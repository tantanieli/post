from django.forms import CharField, ModelForm, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Record
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs) #вызов конструктора родительского метода
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class RecordForm(ModelForm):
    class Meta:
        model = Record
        exclude = ['date']


class PartialNewPostForm(ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'content']