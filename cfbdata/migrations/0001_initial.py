# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'cfbdata_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mascot_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('win_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('loss_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'cfbdata', ['Team'])

        # Adding model 'Game'
        db.create_table(u'cfbdata_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cfbdata.Team'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('team_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('opponent_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('win', self.gf('django.db.models.fields.NullBooleanField')(default='NULL', null=True, blank=True)),
        ))
        db.send_create_signal(u'cfbdata', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'cfbdata_team')

        # Deleting model 'Game'
        db.delete_table(u'cfbdata_game')


    models = {
        u'cfbdata.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opponent_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cfbdata.Team']"}),
            'team_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.NullBooleanField', [], {'default': "'NULL'", 'null': 'True', 'blank': 'True'})
        },
        u'cfbdata.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loss_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mascot_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'win_total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cfbdata']