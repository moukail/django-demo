from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Seed initial users'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin', password='admin123')
        if not User.objects.filter(username='johndoe').exists():
            User.objects.create_user(username='johndoe', password='password')
        self.stdout.write(self.style.SUCCESS("Users created"))