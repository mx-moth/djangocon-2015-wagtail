from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtailnews.models import AbstractNewsItem, NewsIndexMixin
from wagtailnews.decorators import newsindex


@newsindex
class NewsIndex(NewsIndexMixin, Page):
    newsitem_model = 'NewsItem'


class NewsItem(AbstractNewsItem):
    title = models.CharField(max_length=255)
    body = RichTextField()

    panels = AbstractNewsItem.panels + [
        FieldPanel('title'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title
