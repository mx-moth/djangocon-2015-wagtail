from django.db import models
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


@register_snippet
class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ForeignKey(
        'wagtailimages.Image', related_name='+',
        on_delete=models.SET_NULL, null=True, blank=False)
    description = RichTextField()

    LEVEL_CHOICES = [
        ('1-platinum', 'Platinum'),
        ('2-gold', 'Gold'),
        ('3-standard', 'Standard'),
        ('4-contributor', 'Contributor'),
        ('5-in-kind', 'In-kind'),
        ('6-coffee', 'Coffee charity'),
    ]
    level = models.CharField(choices=LEVEL_CHOICES, max_length=20)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        ImageChooserPanel('image'),
        FieldPanel('description'),
        FieldPanel('level'),
    ]

    def __str__(self):
        return self.name

