import datetime
import os
import shutil

from django.conf import settings
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone

from wagtail.wagtailimages.models import Image
from wagtail.wagtailcore.models import Site

from content.models import ContentPage
from sponsors.models import Sponsor, SponsorPage
from schedule.models import Event
from news.models import NewsIndex, NewsItem

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
        self.create_sponsors()
        self.create_schedule()
        self.create_news()

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

        self.sponsors = SponsorPage(
            title='Sponsors',
            slug='sponsors',
            show_in_menus=True,
            body="""
                <h1>Sponsors</h1>
                <p>PyCon Australia gratefully acknowledges the support of our sponsors, without which the conference could not go ahead:</p>
            """)
        self.root_page.add_child(instance=self.sponsors)

        self.newsindex = NewsIndex(
            title='Media',
            slug='media',
            show_in_menus=True)
        self.root_page.add_child(instance=self.newsindex)

    def populate_homepage(self):
        self.root_page.big_text = "PyCon Australia is the national conference for users of the Python programming language"
        self.root_page.banner_image = Image.objects.create(
            title="PyCon people",
            file=self.get_standard_image('banner-default.png'))
        self.root_page.registrations_open = True
        self.root_page.registrations_link = self.registrations
        self.root_page.sponsor_link = self.sponsors
        self.root_page.save()

    def create_sponsors(self):
        Sponsor.objects.create(
            name='Red Hat Asia Pacific',
            url='https://redhat.com.au/',
            level="1-platinum",
            description="""
                <p>Red Hat's mission is to be the catalyst in communities of customers, contributors, and partners creating better technology the open source way. Free and open source creates better software. That's why Red Hat collaborates to build better technology the open source way, regardless of where it is hosted or who started it. We collaborate, and the best technology wins. That's good -- not just for Red Hat, but for everyone.</p>
                <p>Red Hat is proud to be an active supporter of PyCon Australia and a contributor to the Python Community.</p>
            """,
            image=Image.objects.create(
                title="Red Hat logo",
                file=self.get_standard_image("red_hat.png")))
        Sponsor.objects.create(
            name='Takeflight',
            url='http://takeflight.com.au/',
            level="2-gold",
            description="""
                <p>Takeflight are a team of web developers in Hobart, Tasmania. We create highly customised, engaging and innovative websites and web applications using Python, Django and Wagtail as our technologies of choice.</p>
                <p>Our clients represent a broad range of industry sectors, such as education, government, tourism and science. We take pride in delivering stunning, responsive, accessible designs, and robust and secure systems.</p>
                <p>We'll be around at PyCon AU, be sure to say hi!</p>
            """,
            image=Image.objects.create(
                title="Takeflight lgoo",
                file=self.get_standard_image("takeflight.png")))

    def create_schedule(self):
        Event.objects.create(
            name='Mini-Conferences',
            start_date=datetime.date(2015, 7, 31),
            end_date=datetime.date(2015, 7, 31))
        Event.objects.create(
            name='Presentations',
            start_date=datetime.date(2015, 8, 1),
            end_date=datetime.date(2015, 8, 2))
        Event.objects.create(
            name='Sprints',
            start_date=datetime.date(2015, 8, 3),
            end_date=datetime.date(2015, 8, 4))

    def create_news(self):
        NewsItem.objects.create(
            newsindex=self.newsindex,
            date=datetime.datetime(2015, 7, 24, 17, 42, tzinfo=timezone.get_current_timezone()),
            title='Teacher assistance program',
            body="""
                <p>As part of Carrie Anne Philbin’s keynote announcement last week, we also announced the availability of financial assistance grants for qualified primary and secondary teachers wishing to attend the Python in Education Miniconf on July 31st.</p>
                <p>Teachers that are interested in attending the Python in Education Miniconf, but face financial barriers to doing so, are strongly encouraged to apply for financial assistance.</p>
                <p>These grants are made possible by the generous contributions of the Python Software Foundation and Code Club Australia, and are designed to make it easier for teachers to justify attending an education focused event hosted by a software development conference. As such, teachers may apply not only for assistance with registration, travel, and accommodation costs as described for the regular financial assistance program, but also a contribution of up to $360 towards the costs of hiring a substitute teacher for the day.</p>
            """)
        NewsItem.objects.create(
            newsindex=self.newsindex,
            date=datetime.datetime(2015, 7, 13, 16, 17, tzinfo=timezone.get_current_timezone()),
            title='Keynote Speaker: Carrie Anne Philbin',
            body="""
                <p>Following on from 2014's inspirational keynote advocating Python for Every Child in Australia as part of the rollout of the Australian Digital Curriculum, this year sees PyCon Australia playing host to its first ever Python in Education miniconf. As part of that event, we are thrilled to announce our second PyCon Australia 2015 keynote speaker: Carrie Anne Philbin, Education Pioneer at the Raspberry Pi Foundation, chair of the UK's Computing at School's #include initiative, author of "Adventures in Raspberry Pi", and a member of the Board of Directors for the Python Software Foundation.</p>
                <p>As an award winning secondary Computing & ICT teacher, Carrie Anne is a vocal advocate for the merits of Python as an educational tool, and brings to PyCon Australia a wealth of experience with the UK's search for a suitable text based programming language to serve as a follow on from self-contained visual programming environments like Scratch.</p>
            """)

    def get_standard_image(self, name):
        if not os.path.exists(images_dest_dir):
            os.makedirs(images_dest_dir)

        shutil.copyfile(os.path.join(images_src_dir, name),
                        os.path.join(images_dest_dir, name))

        return os.path.join(images_dir_name, name)
