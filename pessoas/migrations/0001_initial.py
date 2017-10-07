# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-31 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangoplus.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enderecos', '0006_auto_20170605_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Nome')),
                ('documento', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Documento')),
                ('telefone', djangoplus.db.models.fields.PhoneField(blank=True, max_length=255, null=True, verbose_name='Telefone')),
                ('email', djangoplus.db.models.fields.EmailField(blank=True, max_length=255, null=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=djangoplus.db.models.fields.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enderecos.Endereco', verbose_name='Endere\xe7o'),
        ),
    ]