from django.core.management import BaseCommand
from django.contrib.auth.models import User

from wagtail.wagtailcore.models import Site

from content.models import ContentPage


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', email='', password='p')

        site = Site.objects.get(is_default_site=True)
        root_page = site.root_page

        about = ContentPage(
            title='About',
            slug='about',
            show_in_menus=True,
            body="""
            <h1>About PyCon Australia</h1>
            <p>PyCon Australia is the national conference for the Python Programming Community. The sixth PyCon Australia will be held from July 31st to August 4th, 2015 in Brisbane, bringing together professional, student and enthusiast developers with a love for developing with Python. PyCon Australia informs the country’s Python developers with presentations, tutorials and panel sessions by experts and core developers of Python, as well as the libraries and frameworks that they rely on.</p>
            <p>PyCon Australia is presented by <a href="http://www.linux.org.au">Linux Australia</a>.</p>
            """)
        root_page.add_child(instance=about)

        team = ContentPage(
            title='Team',
            slug='team',
            show_in_menus=True,
            body="""
                <h1>Team</h1>
                <h2>Organising team</h2>
                <ul>
                <li>Lead - Clinton Roy
                </li><li>Treasurer - Russell Stuart
                </li><li>Video - Matthew Franklin
                </li><li>Keynotes - Nick Coghlan
                </li><li>Sponsorship - Chris Neugebauer
                </li><li>Graphics - Nicole Harris
                </li><li>Programme Committee Chair - Richard Jones
                </li></ul>
            """)
        about.add_child(instance=team)

        venue = ContentPage(
            title='Venue',
            slug='venue',
            show_in_menus=True,
            body="""
                <h1>Venue</h1>
                <p>Our venue for 2015 is the Pullman Hotel, the largest combined hotel and conference centre located smack bang in the middle of the city.</p>
                <p>The Pullman is directly opposite central bus stations, very close to rail and nearby to citycat catamaran.</p>
                <p>There's plenty of coffee, food and drink available within the hotel and in the Queen Street Mall, just a block away.</p>
            """)
        about.add_child(instance=venue)
