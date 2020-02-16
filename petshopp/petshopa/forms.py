from django import forms
from .models import PetShop

class PetForm(forms.ModelForm):
    class Meta:
        model = PetShop
        fields = '__all__'
