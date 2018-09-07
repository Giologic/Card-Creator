from django import forms

from .models import Card

class CardForm(forms.ModelForm):
	"""
	Description: 
	Class representation of an HTML Form

	Form fields:
	character_name:varchar 	- Text Input
	description:varchar 	- Text Area
	hitpoints:int 			- Text Input
	cost:int 				- Text Input
	deploy_time:float 		- Text Input
	damage:int 				- Text Input
	"""

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
		"""
		Description:

		Defines the metadata for the Model
		"""
		model = Card  
		fields = ('character_name','description','hitpoints','cost','deploy_time','damage',) 