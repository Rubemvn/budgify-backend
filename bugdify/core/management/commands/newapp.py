import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):
    help = "Creates a new app using the custom template in the current directory"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the new app')

    def handle(self, *args, **options):
        app_name = options['name']
        template_path = os.path.join(settings.BASE_DIR, 'app_template')
        call_command('startapp', app_name, template=template_path)
        self.stdout.write(self.style.SUCCESS(f"App '{app_name}' created"))

