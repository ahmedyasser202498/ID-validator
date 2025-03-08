from django.core.management.base import BaseCommand
from nid_validator.models import APIKey

class Command(BaseCommand):
    help = 'Generate an API key'

    def handle(self,*args, **options):
        # Generate an API key here
        if not APIKey.objects.filter(description='My Validator API key', is_active=True):
            api_key = APIKey.objects.create(key='1111', description='My Validator API key', is_active=True)
            self.stdout.write(self.style.SUCCESS(f'Generated API key: {api_key.key}'))
