import os
import shutil

from django.conf import settings
from django.core.management import BaseCommand
from django.contrib.auth.models import User

from wagtail.wagtailimages.models import Image
from wagtail.wagtailcore.models import Site

from content.models import ContentPage

dirname = os.path.dirname
here_dir = dirname(__file__)
base_dir = dirname(dirname(dirname(here_dir)))
images_dir_name = 'sample_images'
images_src_dir = os.path.join(dirname(base_dir), 'images')
images_dest_dir = os.path.join(settings.MEDIA_ROOT, images_dir_name)



class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', email='', password='p')

        site = Site.objects.get(is_default_site=True)
        self.root_page = site.root_page.specific

        self.create_pages()
        self.populate_homepage()

    def create_pages(self):
        about = ContentPage(
            title='About',
            slug='about',
            show_in_menus=True,
            body="""
            <h1>About PyCon Australia</h1>
            <p>PyCon Australia is the national conference for the Python Programming Community. The sixth PyCon Australia will be held from July 31st to August 4th, 2015 in Brisbane, bringing together professional, student and enthusiast developers with a love for developing with Python. PyCon Australia informs the country’s Python developers with presentations, tutorials and panel sessions by experts and core developers of Python, as well as the libraries and frameworks that they rely on.</p>
            <p>PyCon Australia is presented by <a href="http://www.linux.org.au">Linux Australia</a>.</p>
            """)
        self.root_page.add_child(instance=about)

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

        self.registrations = ContentPage(
            title='Register',
            slug='register',
            show_in_menus=True,
            body="""
            <h1>Prices</h1>
            <p>To register, you will need to create an account and then register. All registrations are subject to the conference terms and conditions.</p>
            """)
        self.root_page.add_child(instance=self.registrations)

    def populate_homepage(self):
        self.root_page.big_text = "PyCon Australia is the national conference for users of the Python programming language"
        self.root_page.banner_image = Image.objects.create(
            title="PyCon people",
            file=self.get_standard_image('banner-default.png'))
        self.root_page.registrations_open = True
        self.root_page.registrations_link = self.registrations
        self.root_page.sponsor_link = self.registrations
        self.root_page.save()

    def get_standard_image(self, name):
        if not os.path.exists(images_dest_dir):
            os.makedirs(images_dest_dir)

        shutil.copyfile(os.path.join(images_src_dir, name),
                        os.path.join(images_dest_dir, name))

        return os.path.join(images_dir_name, name)
