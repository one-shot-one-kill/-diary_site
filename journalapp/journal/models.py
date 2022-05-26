from django.db import models
from django.urls import reverse_lazy


class Journal(models.Model):
	title = models.CharField(max_length=100, blank=False)
	description = models.TextField()
	data_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['data_created']

	def __str__(self):
		return self.title