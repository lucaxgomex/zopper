from django.db import models

# Create your models here.
class Register(models.Model):
	name = models.CharField(max_length=300)
	get_url = models.URLField(max_length=300)
	date = models.DateField(auto_now_add=True)
