# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 14:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 4, 13, 14, 32, 22, 26558, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='all', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Category'),
        ),
    ]
