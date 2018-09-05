from django.db import models

# Create your models here.
class Card(models.Model):
	character_name = models.CharField(max_length=30)
	description = models.CharField(max_length=3000)
	hitpoints = models.IntegerField(default=1)
	cost = models.IntegerField(default=1)
	deploy_time = models.FloatField(default = 0.0)
	damage = models.IntegerField(default=1)


	def __str__(self):
		string_builder = "ID# " + str(self.id) + " - " + self.character_name
		return string_builder

	class Meta:
		"""docstring for Meta"""
		db_table = "card"
			