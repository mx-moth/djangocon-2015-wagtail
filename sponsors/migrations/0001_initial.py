# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('level', models.CharField(choices=[('1-platinum', 'Platinum'), ('2-gold', 'Gold'), ('3-standard', 'Standard'), ('4-contributor', 'Contributor'), ('5-in-kind', 'In-kind'), ('6-coffee', 'Coffee charity')], max_length=20)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', null=True)),
            ],
        ),
    ]
