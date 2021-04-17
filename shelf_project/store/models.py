from django.db import models

# Create your models here.
from django.db import models

class livre(models.Model):
	titre = models.CharField(max_length=255)
	
	def __str__(self):
		return self.titre

