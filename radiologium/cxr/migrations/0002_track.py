# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cxr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=b'Users/abiramnair/Desktop/Radiologium/radiologium/radiologium/cxr/images')),
            ],
        ),
    ]