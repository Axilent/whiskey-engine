""" 
Models for Whiskey Engine.
"""
import datetime
from django.conf import settings
from django.db import models
from djax.content import ACEContent, ContentManager

class Whiskey(models.Model,ACEContent):
    """ 
    Whiskey!
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField()
    category = models.CharField(max_length=100)
    
    bite = models.FloatField()
    candy = models.FloatField()
    complexity = models.FloatField()
    flowers = models.FloatField()
    fruit = models.FloatField()
    herbs_spice = models.FloatField()
    length_of_finish = models.FloatField()
    smoothness = models.FloatField()
    sweet = models.FloatField()
    wood = models.FloatField()
    
    bottle = models.CharField(null=True,max_length=500)
    thumb = models.CharField(null=True, max_length=500)
    
    objects = ContentManager()
    
    def __unicode__(self):
        return self.name
    
    class ACE:
        content_type = 'Whiskey'
        field_map = {
            'name':'name',
            'description':'description',
            'slug':'slug',
            'category':'category',
            'bite':'bite',
            'candy':'candy',
            'complexity':'complexity',
            'flowers':'flowers',
            'fruit':'fruit',
            'herbs_spice':'herbs_spice',
            'length_of_finish':'length_of_finish',
            'smoothness':'smoothness',
            'sweet':'sweet',
            'wood':'wood',
            'bottle':'bottle',
            'thumb':'thumb',
        }
