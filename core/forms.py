from django import forms
from .models import Emp

class addempForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ('emp_id','emp_name','city')
        widgets = {
          'emp_name': forms.TextInput(attrs={'class':'form-control'}),
          'emp_id': forms.TextInput(attrs={'class':'form-control'}),
          'city': forms.TextInput(attrs={'class':'form-control'})
        }

