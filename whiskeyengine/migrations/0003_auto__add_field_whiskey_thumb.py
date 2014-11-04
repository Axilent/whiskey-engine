# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Whiskey.thumb'
        db.add_column(u'whiskeyengine_whiskey', 'thumb',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Whiskey.thumb'
        db.delete_column(u'whiskeyengine_whiskey', 'thumb')


    models = {
        u'whiskeyengine.whiskey': {
            'Meta': {'object_name': 'Whiskey'},
            'bite': ('django.db.models.fields.FloatField', [], {}),
            'bottle': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'candy': ('django.db.models.fields.FloatField', [], {}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'complexity': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'flowers': ('django.db.models.fields.FloatField', [], {}),
            'fruit': ('django.db.models.fields.FloatField', [], {}),
            'herbs_spice': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_of_finish': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'smoothness': ('django.db.models.fields.FloatField', [], {}),
            'sweet': ('django.db.models.fields.FloatField', [], {}),
            'thumb': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'wood': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['whiskeyengine']