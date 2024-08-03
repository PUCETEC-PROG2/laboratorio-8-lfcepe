from django import forms
from .models import Pokemon, Trainer

class Pokemon_Form(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        widgets = {
            'name': forms.TextInput (attrs={'class': 'form-control'}),
            'type': forms.Select (attrs={'class': 'form-control'}),
            'weight': forms.NumberInput (attrs={'class': 'form-control'}),
            'height': forms.NumberInput (attrs={'class': 'form-control'}),
            'trainer': forms.Select (attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput (attrs={'class': 'form-control-file'}),
        }

class Trainer_Form(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'last_name','birth_date', 'level', 'details', 'picture']
        widgets = {
            'name': forms.TextInput (attrs={'class': 'form-control'}),
            'last_name': forms.TextInput (attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'level': forms.NumberInput (attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput (attrs={'class': 'form-control-file'}),
        }