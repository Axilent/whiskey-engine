# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Whiskey'
        db.create_table(u'whiskeyengine_whiskey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bite', self.gf('django.db.models.fields.FloatField')()),
            ('candy', self.gf('django.db.models.fields.FloatField')()),
            ('complexity', self.gf('django.db.models.fields.FloatField')()),
            ('flowers', self.gf('django.db.models.fields.FloatField')()),
            ('fruit', self.gf('django.db.models.fields.FloatField')()),
            ('herbs_spice', self.gf('django.db.models.fields.FloatField')()),
            ('length_of_finish', self.gf('django.db.models.fields.FloatField')()),
            ('smoothness', self.gf('django.db.models.fields.FloatField')()),
            ('sweet', self.gf('django.db.models.fields.FloatField')()),
            ('wood', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'whiskeyengine', ['Whiskey'])


    def backwards(self, orm):
        # Deleting model 'Whiskey'
        db.delete_table(u'whiskeyengine_whiskey')


    models = {
        u'whiskeyengine.whiskey': {
            'Meta': {'object_name': 'Whiskey'},
            'bite': ('django.db.models.fields.FloatField', [], {}),
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
            'wood': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['whiskeyengine']