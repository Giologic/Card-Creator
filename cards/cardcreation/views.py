from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Card
from .forms import CardForm
# Create your views here.
# class CardsIndexView(generic.ListView):
# 	template_name = 'cardcreation/index.html'
# 	context_object_name = 'cards_list'

# 	def get_queryset(self):
# 		return Card.objects.order_by('-id')


#Display Cards
def index(request):
	card_list = Card.objects.order_by('id')
	# field_list = Card._meta.get_fields()
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
	form = CardForm() 
	if request.method == "POST":
		form = CardForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('cardcreation:index')
			except:
				pass
		else:
			card = CardForm()
	return render(request,'cardcreation/create.html', {'form': form})

#Edit a Card
def edit_card(request, id):
	card = get_object_or_404(Card, id = id)

	if request.method == "POST":
		form = CardForm(request.POST, instance = card)

		if form.is_valid():
			try:
				form.save()
				return redirect('cardcreation:index')
			except:
				pass
	else: 
		form = CardForm(instance = card)
		# return redirect("cardcreation:index")
	context = {
		'form' : form,
		'card' : card,
	}
	
	return render(request, 'cardcreation/edit.html', context)


def delete_card(request, id):
    card = Card.objects.get(id=id)  
    card.delete()  
    return redirect("cardcreation:index")  
