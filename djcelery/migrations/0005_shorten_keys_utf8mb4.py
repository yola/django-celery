# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Shorten indecies to fit in MySQL utf8mb4 columns
        # Retroactively done in previous migrations, so that they can be run,
        # at all.
        db.alter_column(u'celery_taskmeta', 'task_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36))
        db.alter_column(u'celery_tasksetmeta', 'taskset_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36))
        db.alter_column('djcelery_workerstate', 'hostname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=191))

    def backwards(self, orm):
        db.alter_column(u'celery_taskmeta', 'task_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True))
        db.alter_column(u'celery_tasksetmeta', 'taskset_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255))
        db.alter_column('djcelery_workerstate', 'hostname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255))

    models = {
        'djcelery.crontabschedule': {
            'Meta': {'ordering': "[u'month_of_year', u'day_of_month', u'day_of_week', u'hour', u'minute']", 'object_name': 'CrontabSchedule'},
            'day_of_month': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'day_of_week': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'hour': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'month_of_year': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'})
        },
        'djcelery.intervalschedule': {
            'Meta': {'ordering': "[u'period', u'every']", 'object_name': 'IntervalSchedule'},
            'every': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'djcelery.periodictask': {
            'Meta': {'object_name': 'PeriodicTask'},
            'args': ('django.db.models.fields.TextField', [], {'default': "u'[]'", 'blank': 'True'}),
            'crontab': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djcelery.CrontabSchedule']", 'null': 'True', 'blank': 'True'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'exchange': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djcelery.IntervalSchedule']", 'null': 'True', 'blank': 'True'}),
            'kwargs': ('django.db.models.fields.TextField', [], {'default': "u'{}'", 'blank': 'True'}),
            'last_run_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'queue': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'routing_key': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'total_run_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'djcelery.periodictasks': {
            'Meta': {'object_name': 'PeriodicTasks'},
            'ident': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'unique': 'True', 'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {})
        },
        'djcelery.taskmeta': {
            'Meta': {'object_name': 'TaskMeta', 'db_table': "u'celery_taskmeta'"},
            'date_done': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('djcelery.picklefield.PickledObjectField', [], {'default': 'None', 'null': 'True'}),
            'result': ('djcelery.picklefield.PickledObjectField', [], {'default': 'None', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '50'}),
            'task_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'}),
            'traceback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'djcelery.tasksetmeta': {
            'Meta': {'object_name': 'TaskSetMeta', 'db_table': "u'celery_tasksetmeta'"},
            'date_done': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('djcelery.picklefield.PickledObjectField', [], {}),
            'taskset_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'})
        },
        'djcelery.taskstate': {
            'Meta': {'ordering': "[u'-tstamp']", 'object_name': 'TaskState'},
            'args': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'eta': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kwargs': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'db_index': 'True'}),
            'result': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'retries': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'runtime': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'task_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'}),
            'traceback': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'tstamp': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djcelery.WorkerState']", 'null': 'True'})
        },
        'djcelery.workerstate': {
            'Meta': {'ordering': "[u'-last_heartbeat']", 'object_name': 'WorkerState'},
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '191'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_heartbeat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['djcelery']
