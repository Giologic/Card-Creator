from django.urls import path
from . import views

app_name='cardcreation'

urlpatterns = [
	path('', views.index, name='index'),
	path('create/', views.create_card, name='create'),
	path('edit/<int:id>', views.edit_card, name='edit'),
	path('update/<int:id>', views.update_card, name='update'),
	path('delete/<int:id>', views.delete_card, name='delete'),
]