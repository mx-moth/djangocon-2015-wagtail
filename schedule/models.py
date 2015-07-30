from django.db import models
from wagtail.wagtailsnippets.models import register_snippet


@register_snippet
class Event(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
