from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=120, default="a")
	date = models.CharField(max_length=120, default="a")
	def _unicode_(self):
		return self.name
