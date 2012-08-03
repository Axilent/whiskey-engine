import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models import Avg

#from imagekit.models import ImageModel

# class Category(models.Model):
#     """
#     A general category of whiskey.
#     """
#     name = models.CharField(max_length=100,unique=True)
#     slug = models.SlugField(unique=True)
#     description = models.TextField(blank=True)
# 
#     def __unicode__(self):
#         return self.name
# 
#     @models.permalink
#     def get_absolute_url(self):
#         return ('whiskeyengine.views.category', [self.slug])
# 
#     class Meta:
#         verbose_name_plural = 'categories'
# 
# class Distillery(models.Model):
#     """
#     A producer of whiskey.
#     """
#     name = models.CharField(unique=True,max_length=100)
# 
#     def __unicode__(self):
#         return self.name
# 
#     class Meta:
#         verbose_name_plural = 'distilleries'
# 
# class WhiskeyManager(models.Manager):
#     """
#     Manager class for whiskey.
#     """
#     def get_whiskey_by_sliders(self,smooth,bite,sweet):
#         """
#         Gets whiskey by slider value.  Slider values are on a scale of
#         0 to 100.
#         """
#         smooth_value = round((8.0 * float(smooth) / 100.0) + 2.0) / 2.0
#         bite_value = round((8.0 * float(bite) / 100.0) + 2.0) / 2.0
#         sweet_value = round((8.0 * float(sweet) / 100.0) + 2.0) / 2.0
#         
#         whiskey = None
#         
#         # Attempt precise lookup
#         whiskey_results = self.filter(Q(smoothness=smooth_value),
#                                       Q(Q(herbs_spice=bite_value) | Q(wood=bite_value)),
#                                       Q(Q(candy=sweet_value) | Q(flowers=sweet_value) | Q(fruit=sweet_value))).order_by('?')
#         
#         if len(whiskey_results):
#             print 'exact slider match'
#             return whiskey_results[0]
#         else:
#             # create ranges
#             smooth_min = max(smooth_value - 0.5,0.0)
#             smooth_max = min(smooth_value + 0.5,5.0)
#             bite_min = max(bite_value - 0.5,0.0)
#             bite_max = min(bite_value + 0.5,5.0)
#             sweet_min = max(sweet_value - 0.5,0.0)
#             sweet_max = min(sweet_value + 0.5,5.0)
#             
#             # Range query
#             smooth_clause = Q(Q(smoothness__gte=smooth_min) & Q(smoothness__lte=smooth_max))
#             
#             herbs_spice_clause = Q(Q(herbs_spice__gte=bite_min) & Q(herbs_spice__lte=bite_max))
#             wood_clause = Q(Q(wood__gte=bite_min) & Q(wood__lte=bite_max))
#             bite_clause = Q(herbs_spice_clause | wood_clause)
#             
#             candy_clause = Q(Q(candy__gte=sweet_min) & Q(candy__lte=sweet_max))
#             flowers_clause = Q(Q(flowers__gte=sweet_min) & Q(flowers__lte=sweet_max))
#             fruit_clause = Q(Q(fruit__gte=sweet_min) & Q(fruit__lte=sweet_max))
#             sweet_clause = Q(candy_clause | flowers_clause | fruit_clause)            
#             
#             whiskey_results = self.filter(smooth_clause,
#                                           bite_clause,
#                                           sweet_clause).order_by('?')
#             
#             if len(whiskey_results):
#                 print 'range slider match'
#                 return whiskey_results[0]
#             else:
#                 raise Whiskey.DoesNotExist
# 
# class Whiskey(models.Model):
#     """
#     A whiskey.
#     """
#     distillery = models.ForeignKey(Distillery,related_name='whiskeys', null=True, blank=True)
#     name = models.CharField(max_length=100,unique=True)
#     slug = models.SlugField(unique=True)
#     description = models.TextField(blank=True)
#     bottle = models.ImageField(upload_to=settings.UPLOAD_PATH, blank=True)
#     thumb = models.ImageField(upload_to=settings.UPLOAD_PATH, blank=True)
#     category = models.ForeignKey(Category,related_name='whiskeys',null=True, blank=True)
#     saaspire_key = models.CharField(null=True,unique=True, max_length=100)
# 
#     # Tasting Metadata
#     herbs_spice = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     flowers = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     fruit = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     candy = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     wood = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     length_of_finish = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     complexity = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     smoothness = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#     
#     objects = WhiskeyManager()
# 
#     class Meta:
#         ordering = ['name']
# 
#     # class IKOptions:
#     #     spec_module = 'whiskeyengine.specs'
#     #     cache_dir = 'bottle_photos'
#     #     image_field = 'bottle'
# 
#     @property
#     def average_rating(self):
#         avr = self.reviews.aggregate(Avg('rating'))['rating__avg']
#         return 0 if avr is None else int(round(avr))
# 
#     @property
#     def average_rating_list(self):
#         return xrange(self.average_rating)
# 
#     @property
#     def cousins(self):
#         """
#         Gets other whiskeys made by the same distillery as this whiskey.
#         """
#         return self.distillery.whiskeys.exclude(pk=self.pk)
# 
#     def has_reviewed(self,drinker):
#         """
#         Test to determine if the specified drinker has reviewed  this whiskey.
#         """
#         return self.reviews.filter(reviewer=drinker).count()
# 
#     def __unicode__(self):
#         return self.name
# 
#     @models.permalink
#     def get_absolute_url(self):
#         return ('whiskeyengine.views.whiskey', [self.slug])
#     
#     @property
#     def smooth_percent(self):
#         return self.smoothness * 20
#     
#     @property
#     def bite_percent(self):
#         return (self.herbs_spice + self.wood) * 10
#     
#     @property
#     def sweet_percent(self):
#         return (self.candy + self.flowers + self.fruit) * 20 / 3
#     
# 
# class Feature(models.Model):
#     """
#     A point to feature on the site.
#     """
#     name = models.CharField(primary_key=True,max_length=100)
#     whiskey = models.ForeignKey(Whiskey,null=True)
# 
#     def __unicode__(self):
#         return '%s: %s' % (self.name,unicode(self.whiskey))
# 
# class Drinker(models.Model):
#     """
#     Someone who drinks whiskey.
#     """
#     user = models.ForeignKey(User,unique=True)
#     shelf = models.ManyToManyField(Whiskey,related_name='drinkers',null=True,blank=True)
#     saaspire_profile = models.CharField(null=True,blank=True, max_length=100)
# 
#     def __unicode__(self):
#         return self.user.username
# 
# class Review(models.Model):
#     """
#     A review of a whiskey.
#     """
#     reviewer = models.ForeignKey(Drinker,related_name='reviews')
#     whiskey = models.ForeignKey(Whiskey,related_name='reviews')
#     rating = models.IntegerField()
#     comments = models.TextField(blank=True)
#     created = models.DateTimeField(blank=True, default=datetime.datetime.now)
# 
#     def __unicode__(self):
#         return '%s by %s: %d stars' % (unicode(self.whiskey),unicode(self.reviewer),self.rating)
# 
#     class Meta:
#         get_latest_by = 'created'
