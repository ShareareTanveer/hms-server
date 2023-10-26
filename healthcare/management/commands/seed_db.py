from django.core.management.base import BaseCommand, CommandError
from django.db import connections
import os
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Seed data for the shop app from an SQL file'

    def handle(self, *args, **options):
        # Open the SQL file and read its contents
        current_dir = os.path.dirname(__file__)
        all_file = os.path.join(current_dir, 'all.sql')

        # Get the database connection
        connection = connections['default']

        # Execute the SQL commands
        with open(all_file, 'r') as f:
            sql_statements = f.read().split(';')

            for sql in sql_statements:
                sql = sql.strip()

                if not sql:
                    continue

                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sql)
                except IntegrityError as e:
                    self.stderr.write(f'Skipping invalid SQL statement: {sql}')
                    self.stderr.write(str(e))

        # Print a success message
        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))