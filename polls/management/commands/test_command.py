from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('door', type=int, choices=range(1, 10))
        parser.add_argument('--foo', required=True)

    def handle(self, *args, **options):

        # self.stdout.write(self.style.SUCCESS(f"Args: {options['test_args']}"))
        self.stdout.write(self.style.SUCCESS(f"Args: {options['door']}"))
