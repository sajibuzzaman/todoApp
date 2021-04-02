from django.forms import ModelForm
from django import forms

from app.models import TODO
class TODOForm(ModelForm):
    title= forms.CharField(widget= forms.TextInput( attrs={'placeholder':'Task title...'}))
    due= forms.DateTimeField(widget= forms.DateInput(attrs={'placeholder':'Due date...',}), required=False)

    class Meta:
        model = TODO
        fields = ['title' , 'status' , 'priority', 'due']