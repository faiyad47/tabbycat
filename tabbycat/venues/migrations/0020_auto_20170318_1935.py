# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0019_auto_20170228_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venueconstraintcategory',
            name='venues',
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'ordering': ['name'], 'verbose_name': 'venue', 'verbose_name_plural': 'venues'},
        ),
        migrations.AlterModelOptions(
            name='venueconstraint',
            options={'verbose_name': 'venue constraint', 'verbose_name_plural': 'venue constraints'},
        ),
        migrations.RemoveField(
            model_name='venue',
            name='group',
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=40, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='priority',
            field=models.IntegerField(help_text='Venues with a higher priority number will be preferred when allocating venues to debates', verbose_name='priority'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='tournament',
            field=models.ForeignKey(blank=True, help_text='Venues not assigned to any tournament can be shared between tournaments', null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament'),
        ),
        migrations.AlterField(
            model_name='venueconstraint',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.VenueCategory', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='venueconstraint',
            name='priority',
            field=models.IntegerField(verbose_name='priority'),
        ),
        migrations.AlterField(
            model_name='venueconstraint',
            name='subject_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='subject content type'),
        ),
        migrations.AlterField(
            model_name='venueconstraint',
            name='subject_id',
            field=models.PositiveIntegerField(verbose_name='subject ID'),
        ),
        migrations.DeleteModel(
            name='VenueConstraintCategory',
        ),
        migrations.DeleteModel(
            name='VenueGroup',
        ),
    ]