from django import forms
from app2.models import User #Here User is name o the class in models


class NewUserForm(forms.ModelForm): #here NewUserForm is name o ths class
    
    class Meta():

        model=User
        fields='__all__'