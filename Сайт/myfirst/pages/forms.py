from .models import Task
from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["tittle", "task"]
        widgets = {"tittle": TextInput(attrs = {
                'class':'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs = {
                'class':'form-control',
                'placeholder': 'Введите описание'
            }),     
        }
class UserRegistrationForm(ModelForm):
    password = CharField(label='Password', widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name']

    def clean_password2(self):
        cd = self.cleaned_data
