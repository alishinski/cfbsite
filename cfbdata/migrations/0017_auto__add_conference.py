# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Conference'
        db.create_table(u'cfbdata_conference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conference_code', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('conference_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'cfbdata', ['Conference'])


    def backwards(self, orm):
        # Deleting model 'Conference'
        db.delete_table(u'cfbdata_conference')


    models = {
        u'cfbdata.conference': {
            'Meta': {'object_name': 'Conference'},
            'conference_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'conference_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cfbdata.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 9, 10, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opponent_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'opponent_name': ('django.db.models.fields.CharField', [], {'default': "'opp'", 'max_length': '200'}),
            'opponent_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cfbdata.Team']"}),
            'team_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.NullBooleanField', [], {'default': "'NULL'", 'null': 'True', 'blank': 'True'})
        },
        u'cfbdata.team': {
            'Meta': {'object_name': 'Team'},
            'conference_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loss_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mascot_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team_num_code': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'win_total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cfbdata']