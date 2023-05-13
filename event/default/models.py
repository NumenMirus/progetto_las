from django.db import models
import os
from event.settings import MEDIA_URL
import datetime

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    time_start_at = models.TimeField(null=True, blank=True)
    time_end_at = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    cover_image = models.ImageField(upload_to=os.path.join(MEDIA_URL, 'cover_events/'), blank=True, null=True)

    def set_modified_date(self):
        self.updated_at = datetime.datetime.now()

    def set_created_date(self):
        self.created_at = datetime.datetime.now()