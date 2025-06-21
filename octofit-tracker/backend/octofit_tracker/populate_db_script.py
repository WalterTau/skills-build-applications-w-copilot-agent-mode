from octofit_tracker.test_data import TEST_DATA
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']

    # Clear existing data
    for collection in TEST_DATA:
        db[collection].delete_many({})

    # Insert test data
    for collection, docs in TEST_DATA.items():
        if docs:
            db[collection].insert_many(docs)
            print(f'Inserted {len(docs)} documents into {collection}')
        else:
            print(f'No documents to insert for {collection}')

    print('Database population complete.')
