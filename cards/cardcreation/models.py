from django.db import models

# Create your models here.
class Card(models.Model):
	"""
	Card Fields:

	character_name:varchar(30)
	description:varchar(3000)
	hitpoints:int
	cost:int
	deploy_time:float
	damage:int
	"""

	character_name = models.CharField(max_length=30)
	description = models.CharField(max_length=3000)
	hitpoints = models.IntegerField(default=1)
	cost = models.IntegerField(default=1)
	deploy_time = models.FloatField(default = 0.0)
	damage = models.IntegerField(default=1)


	def __str__(self):
		"""
		Description: Returns this string when an instance of Card is printed (equivalent to Java's .toString() method)
		"""
		return "ID# " + str(self.id) + " - " + self.character_name

	class Meta:
		"""
		Description: Defines the metadata for the model
		"""
		db_table = "card"
			