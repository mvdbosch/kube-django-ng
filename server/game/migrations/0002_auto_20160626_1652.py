# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.IntegerField(choices=[(1, 'Adventure'), (2, 'Action'), (3, 'Fighter'), (4, 'Music'), (5, 'Platformer'), (6, 'Puzzle'), (7, 'Racing'), (8, 'RPG'), (9, 'Sports'), (10, 'Strategy')], default=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.IntegerField(choices=[(1, 'PS4'), (2, 'PS3'), (3, 'PS Vita'), (4, 'WII U'), (5, 'WII'), (6, '3DS'), (7, 'PC'), (8, 'XBONE'), (9, 'XBOX 360'), (10, 'iOS'), (11, 'Android')], default=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
