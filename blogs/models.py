from datetime import datetime
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):

	title = models.CharField(max_length=90)
	slug = models.SlugField()
	author = models.ForeignKey(User, related_name="posts")

	content = models.TextField()

	public = models.BooleanField(default=False)

	created = models.DateTimeField(default=datetime.now)  
	updated = models.DateTimeField(null=True, blank=True) 
	published = models.DateTimeField(null=True, blank=True) 

	view_count = models.IntegerField(default=0, editable=False)


	def __unicode__(self):
		return self.title