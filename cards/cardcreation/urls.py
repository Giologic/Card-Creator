from django.urls import path
from . import views

""" Application name as referred to by cards/urls.py (Global Url Mapper)"""
app_name='cardcreation'

"""
Url patterns for the following request functions:

C - views.create_card
R - views.index
U - views.edit_card
D - views.delete_card

"""
urlpatterns = [
	path('', views.index, name='index'),
	path('create/', views.create_card, name='create'),
	path('edit/<int:id>', views.edit_card, name='edit'),
	path('delete/<int:id>', views.delete_card, name='delete'),
]