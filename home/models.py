from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, PageChooserPanel)

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):

    big_text = models.TextField()
    banner_image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=False)

    registrations_open = models.BooleanField()
    registrations_link = models.ForeignKey(
        Page, on_delete=models.SET_NULL, null=True, blank=False, related_name='+')

    sponsor_link = models.ForeignKey(
        Page, on_delete=models.SET_NULL, null=True, blank=False, related_name='+')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('big_text'),
            ImageChooserPanel('banner_image'),
        ], 'Banner'),
        MultiFieldPanel([
            FieldPanel('registrations_open'),
            PageChooserPanel('registrations_link'),
        ], 'Registrations'),
        PageChooserPanel('sponsor_link'),
    ]

    parent_page_types = []
