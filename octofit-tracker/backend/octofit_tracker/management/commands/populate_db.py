from django.core.management.base import BaseCommand
from octofit_tracker.test_data import TEST_DATA
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate octofit_db with test data.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        for collection in TEST_DATA:
            db[collection].delete_many({})

        # Insert test data
        for collection, docs in TEST_DATA.items():
            if docs:
                db[collection].insert_many(docs)
                self.stdout.write(self.style.SUCCESS(f'Inserted {len(docs)} documents into {collection}'))
            else:
                self.stdout.write(self.style.WARNING(f'No documents to insert for {collection}'))

        self.stdout.write(self.style.SUCCESS('Database population complete.'))
