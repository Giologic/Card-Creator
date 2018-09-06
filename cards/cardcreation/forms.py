from django import forms

from .models import Card

class CardForm(forms.ModelForm):  
	character_name = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Character Name',
		}
	))

	description = forms.CharField(widget=forms.Textarea(
		attrs={
			'class': 'form-control',
			'rows': 2,
			'placeholder': 'Description',
		}
	))
	hitpoints = forms.IntegerField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 50,
		}
	))

	cost = forms.IntegerField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 3,
		}
	))

	deploy_time = forms.FloatField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 1.5,
		}
	))

	damage = forms.IntegerField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 50,
		}
	))

	class Meta:  
		model = Card  
		fields = ('character_name','description','hitpoints','cost','deploy_time','damage',) 