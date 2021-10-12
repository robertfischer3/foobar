from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import uuid

class PhotoOfDay(models.Model):
    '''
    Photo of the Day Model.  Simple representation of data that comes back from the web service
    '''
    id = models.URLField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    photodate = models.DateField(editable=True, unique=True)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=2000)
    # HD URL is not always populated
    hdurl = models.CharField(max_length=2000, null=True, blank=True)
    # Placeholder
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    copyright = models.CharField(max_length=200, null=True, blank=True)
    explanation = models.TextField(max_length=500, null=True, blank=True)
    media_type = models.CharField(max_length=100, null=True, blank=True)
    service_version = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        # Default ordering by photo date
        ordering = ['photodate']

        def __unicode__(self):
            return self.title




