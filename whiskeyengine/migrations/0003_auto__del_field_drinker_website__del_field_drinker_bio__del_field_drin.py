# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Drinker.website'
        db.delete_column('whiskeyengine_drinker', 'website')

        # Deleting field 'Drinker.bio'
        db.delete_column('whiskeyengine_drinker', 'bio')

        # Deleting field 'Drinker.twitter'
        db.delete_column('whiskeyengine_drinker', 'twitter')

        # Deleting field 'Drinker.pic'
        db.delete_column('whiskeyengine_drinker', 'pic')

        # Deleting field 'Drinker.profession'
        db.delete_column('whiskeyengine_drinker', 'profession')

        # Deleting field 'Drinker.blog'
        db.delete_column('whiskeyengine_drinker', 'blog')

        # Deleting field 'Drinker.registered'
        db.delete_column('whiskeyengine_drinker', 'registered')

        # Removing M2M table for field wishlist on 'Drinker'
        db.delete_table('whiskeyengine_drinker_wishlist')


    def backwards(self, orm):
        
        # Adding field 'Drinker.website'
        db.add_column('whiskeyengine_drinker', 'website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Drinker.bio'
        db.add_column('whiskeyengine_drinker', 'bio', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Drinker.twitter'
        db.add_column('whiskeyengine_drinker', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Drinker.pic'
        raise RuntimeError("Cannot reverse this migration. 'Drinker.pic' and its values cannot be restored.")

        # Adding field 'Drinker.profession'
        db.add_column('whiskeyengine_drinker', 'profession', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Drinker.blog'
        db.add_column('whiskeyengine_drinker', 'blog', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Drinker.registered'
        db.add_column('whiskeyengine_drinker', 'registered', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 6, 27, 11, 20, 56, 685497), blank=True), keep_default=False)

        # Adding M2M table for field wishlist on 'Drinker'
        db.create_table('whiskeyengine_drinker_wishlist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('drinker', models.ForeignKey(orm['whiskeyengine.drinker'], null=False)),
            ('whiskey', models.ForeignKey(orm['whiskeyengine.whiskey'], null=False))
        ))
        db.create_unique('whiskeyengine_drinker_wishlist', ['drinker_id', 'whiskey_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'whiskeyengine.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'whiskeyengine.distillery': {
            'Meta': {'object_name': 'Distillery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'whiskeyengine.drinker': {
            'Meta': {'object_name': 'Drinker'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saaspire_profile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shelf': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'drinkers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['whiskeyengine.Whiskey']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'whiskeyengine.feature': {
            'Meta': {'object_name': 'Feature'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'whiskey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['whiskeyengine.Whiskey']", 'null': 'True'})
        },
        'whiskeyengine.review': {
            'Meta': {'object_name': 'Review'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'reviewer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reviews'", 'to': "orm['whiskeyengine.Drinker']"}),
            'whiskey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reviews'", 'to': "orm['whiskeyengine.Whiskey']"})
        },
        'whiskeyengine.whiskey': {
            'Meta': {'ordering': "['name']", 'object_name': 'Whiskey'},
            'bottle': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'candy': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'whiskeys'", 'null': 'True', 'to': "orm['whiskeyengine.Category']"}),
            'complexity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'distillery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'whiskeys'", 'null': 'True', 'to': "orm['whiskeyengine.Distillery']"}),
            'flowers': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'fruit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'herbs_spice': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_of_finish': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'saaspire_key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'smoothness': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'wood': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'})
        }
    }

    complete_apps = ['whiskeyengine']
