# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='big_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='registrations_link',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='registrations_open',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='sponsor_link',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailcore.Page'),
        ),
    ]
