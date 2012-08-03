# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('whiskeyengine_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('whiskeyengine', ['Category'])

        # Adding model 'Distillery'
        db.create_table('whiskeyengine_distillery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('whiskeyengine', ['Distillery'])

        # Adding model 'Whiskey'
        db.create_table('whiskeyengine_whiskey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distillery', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='whiskeys', null=True, to=orm['whiskeyengine.Distillery'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bottle', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='whiskeys', null=True, to=orm['whiskeyengine.Category'])),
            ('herbs_spice', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('flowers', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('fruit', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('candy', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('wood', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('length_of_finish', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('complexity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('smoothness', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
        ))
        db.send_create_signal('whiskeyengine', ['Whiskey'])

        # Adding model 'Feature'
        db.create_table('whiskeyengine_feature', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('whiskey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whiskeyengine.Whiskey'], null=True)),
        ))
        db.send_create_signal('whiskeyengine', ['Feature'])

        # Adding model 'Drinker'
        db.create_table('whiskeyengine_drinker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('registered', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 5, 22, 18, 48, 9, 1268), blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('blog', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('saaspire_profile', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('whiskeyengine', ['Drinker'])

        # Adding M2M table for field shelf on 'Drinker'
        db.create_table('whiskeyengine_drinker_shelf', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('drinker', models.ForeignKey(orm['whiskeyengine.drinker'], null=False)),
            ('whiskey', models.ForeignKey(orm['whiskeyengine.whiskey'], null=False))
        ))
        db.create_unique('whiskeyengine_drinker_shelf', ['drinker_id', 'whiskey_id'])

        # Adding M2M table for field wishlist on 'Drinker'
        db.create_table('whiskeyengine_drinker_wishlist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('drinker', models.ForeignKey(orm['whiskeyengine.drinker'], null=False)),
            ('whiskey', models.ForeignKey(orm['whiskeyengine.whiskey'], null=False))
        ))
        db.create_unique('whiskeyengine_drinker_wishlist', ['drinker_id', 'whiskey_id'])

        # Adding model 'Review'
        db.create_table('whiskeyengine_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reviewer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reviews', to=orm['whiskeyengine.Drinker'])),
            ('whiskey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reviews', to=orm['whiskeyengine.Whiskey'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('whiskeyengine', ['Review'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('whiskeyengine_category')

        # Deleting model 'Distillery'
        db.delete_table('whiskeyengine_distillery')

        # Deleting model 'Whiskey'
        db.delete_table('whiskeyengine_whiskey')

        # Deleting model 'Feature'
        db.delete_table('whiskeyengine_feature')

        # Deleting model 'Drinker'
        db.delete_table('whiskeyengine_drinker')

        # Removing M2M table for field shelf on 'Drinker'
        db.delete_table('whiskeyengine_drinker_shelf')

        # Removing M2M table for field wishlist on 'Drinker'
        db.delete_table('whiskeyengine_drinker_wishlist')

        # Deleting model 'Review'
        db.delete_table('whiskeyengine_review')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
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
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'registered': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 5, 22, 18, 48, 9, 1268)', 'blank': 'True'}),
            'saaspire_profile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shelf': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'drinkers'", 'null': 'True', 'to': "orm['whiskeyengine.Whiskey']"}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wishlist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'wishers'", 'null': 'True', 'to': "orm['whiskeyengine.Whiskey']"})
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
            'Meta': {'object_name': 'Whiskey'},
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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'smoothness': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'wood': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'})
        }
    }

    complete_apps = ['whiskeyengine']
