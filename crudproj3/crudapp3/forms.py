from django import forms
from crudapp3.models import Person
# Create your models here.
class RegForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control border border-dark'}),
            'Age': forms.TextInput(attrs={'class':'form-control border border-success'}),
            'Contact': forms.TextInput(attrs={'class':'form-control border border-warning'}),
            'Location': forms.TextInput(attrs={'class':'form-control border border-danger'}),
        }
    