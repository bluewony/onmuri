# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField as ImageField
from library import uploaded_filepath
import datetime
from django.utils import timezone

# Create your models here.
class Home(models.Model):
    pass

class Photo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = ImageField(upload_to=uploaded_filepath)
    desc = models.TextField(blank=True)

    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Board(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)


class BoardCategory(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)