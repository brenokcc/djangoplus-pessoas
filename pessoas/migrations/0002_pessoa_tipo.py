# -*- coding: utf-8 -*-

# Generated by Django 1.11 on 2017-08-02 10:07


from django.db import migrations
import djangoplus.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='tipo',
            field=djangoplus.db.models.fields.CharField(choices=[['F\xedsica', 'F\xedsica'], ['Jur\xeddica', 'Jur\xeddica']], default='F\xedsica', max_length=255, verbose_name='Tipo'),
            preserve_default=False,
        ),
    ]
