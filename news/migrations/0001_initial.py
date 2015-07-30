# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import wagtail.wagtailcore.fields
import wagtailnews.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsIndex',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='wagtailcore.Page', serialize=False, auto_created=True)),
            ],
            bases=(wagtailnews.models.NewsIndexMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published date')),
                ('title', models.CharField(max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('newsindex', models.ForeignKey(to='wagtailcore.Page')),
            ],
            options={
                'ordering': ('-date',),
                'abstract': False,
            },
        ),
    ]
