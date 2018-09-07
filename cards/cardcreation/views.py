from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Card
from .forms import CardForm


# Create your views here.

#Display Cards
def index(request):
	"""
	Description:
	Displays the list of cards from the database

	Variables: 
	card_list:list - contains the list of cards ordered by id in ascending order
	field_list:list - contains the list of field headers
	context:dict - dictionary containing the variables to be passed in the HTTP request
	"""

	card_list = Card.objects.order_by('id')
	field_list = [
		"ID",
		"Character Name",
		"Description",
		"Hitpoints",
		"Cost",
		"Deploy Time",
		"Damage"
	]

	context = {
		'card_list': card_list,
		'field_list': field_list
	}

	return render(request, 'cardcreation/index.html', context)

#Create a Card
def create_card(request):
	"""
	Description:
	Creates a card and inserts it to the database
	If: form is valid and save is successful, function redirects to index
	Else: page remains the same and error output is shown
	
	Variables: 
	form:CardForm - new instance of CardForm 
	context:dict - dictionary containing the variables to be passed in the HTTP request
	"""

	form = CardForm() 
	if request.method == "POST":
		form = CardForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('cardcreation:index')
			except:
				print("Unexpected error:", sys.exc_info()[0])
    			raise
		else:
			card = CardForm()

	context = {
		'form': form
	}

	return render(request,'cardcreation/create.html', context)

#Edit a Card
def edit_card(request, id):
	"""
	Description:
	Updates the card in the database.
	If: form is valid and save is successful, function redirects to index
	Else: page remains the same and error output is shown

	Variables: 
	card:Card - instance of Card given the id
	form:CardForm - instance of an existing CardForm 
	context:dict - dictionary containing the variables to be passed in the HTTP request
	"""	

	card = get_object_or_404(Card, id = id)

	if request.method == "POST":
		form = CardForm(request.POST, instance = card)
		if form.is_valid():
			try:
				form.save()
				return redirect('cardcreation:index')
			except:
				print("Unexpected error:", sys.exc_info()[0])
    			raise
	else: 
		form = CardForm(instance = card)

	context = {
		'form' : form,
		'card' : card,
	}
	
	return render(request, 'cardcreation/edit.html', context)

#Delete a Card
	"""
	Description:
	Delete the card from the database then redirects to index

	Variables: 
	card:Card - instance of Card given the id
	"""	
def delete_card(request, id):
    card = Card.objects.get(id=id)  
    card.delete()  
    return redirect("cardcreation:index")  
