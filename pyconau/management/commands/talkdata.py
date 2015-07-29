from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', email='', password='p')
