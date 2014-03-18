from django.db import models

class producto(models.Model):
	nombre		= models.CharField(max_length=100)
	descripcion	= models.TextField(max_length=300)
	status		= models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre