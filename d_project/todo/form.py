from django import forms
from .models import Todo

class craeteTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','description']