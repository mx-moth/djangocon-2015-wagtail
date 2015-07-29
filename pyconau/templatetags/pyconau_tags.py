from django import template
from django.template.loader import render_to_string
from wagtail.wagtailcore.models import Site, Page


register = template.Library()


@register.simple_tag(takes_context=True)
def top_menu(context, current_page):
    site = Site.objects.get(is_default_site=True)
    root_page = site.root_page.specific

    return render_to_string("tags/top_menu.html", {
        'site': site,
        'root_page': root_page,
        'current_page': current_page,
        'children': root_page.get_children().live().in_menu(),
    })


@register.simple_tag(takes_context=True)
def side_menu(context, current_page):
    site = Site.objects.get(is_default_site=True)
    root_page = site.root_page.specific
    top_level_pages = root_page.get_children().live()
    ancestors = Page.objects.filter(pk=current_page.pk) \
        | current_page.get_ancestors()

    top_level_ancestor = (ancestors & top_level_pages).first()

    return render_to_string("tags/side_menu.html", {
        'current_page': current_page,
        'ancestor': top_level_ancestor,
        'children': top_level_ancestor.get_children().live().in_menu(),
    })


@register.simple_tag(takes_context=True)
def side_sponsors(context):
    from sponsors.models import Sponsor
    return render_to_string("tags/side_sponsors.html", {
        'sponsors': Sponsor.objects.all().order_by('level', 'name')\
            .filter(level__in=['1-platinum', '2-gold']),
    })


@register.simple_tag(takes_context=True)
def conf_dates(context, class_name='conf-dates'):
    from schedule.models import Event
    return render_to_string("tags/conf_dates.html", {
        'schedule': Event.objects.all().order_by('start_date', 'end_date'),
        'class_name': class_name,
    })
