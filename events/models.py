from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

class Event(models.Model):
	name = models.CharField(max_length=200)
	scheduled_date = models.DateTimeField()
	description = models.TextField()
	regsteration_link = models.URLField()
	image_url = models.URLField(default=None)
	slug = models.SlugField(blank=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		""" while adding articles manually store slug as hacker news url
		"""
		if not self.slug:
			self.slug = slugify(self.name)
		super(Event, self).save(*args, **kwargs)
