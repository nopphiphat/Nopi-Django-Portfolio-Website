from django.db import models

# Create your models here.
class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)

	# Make it possible for the name to be displayed on admin page
	def __str__(self):
		return self.summary
