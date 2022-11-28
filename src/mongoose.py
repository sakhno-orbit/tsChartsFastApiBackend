import logging
import urllib.parse
from pymongo import MongoClient
from src.settings import settings
from src.mock_data import FAKE_DATA

MONGODB_USER = settings.MONGODB_USER
MONGODB_PASSWORD = settings.MONGODB_PASSWORD
MONGODB_HOST = settings.MONGODB_HOST
MONGODB_PORT = settings.MONGODB_PORT

DB_NAME = 'default_db'
COLLECTION_NAME = 'charts'

logger = logging.getLogger()


def populate_db(collection):
    logger.info("-" * 30 + "POPULATE_MONGO" + "-" * 30)
    print("-" * 30 + "POPULATE_MONGO" + "-" * 30)
    # collection.delete_many({})
    try:
        count = collection.count_documents({})
        if count:
            print('ALREADY POPULATED')
            return
        print("FAKEDATA: {}".format(FAKE_DATA))
        result = collection.insert_many(FAKE_DATA).inserted_ids
        print('POPULATED result: {}'.format(len(result)))
        print("POPULATED")
    except Exception as exc:
        logging.error("ERROR populate_db: {}".format(exc))


def init_client():
    try:
        uri = 'mongodb://{0}:{1}@{2}/'.format(
                MONGODB_USER,
                urllib.parse.quote_plus(MONGODB_PASSWORD),
                MONGODB_HOST,
                # MONGODB_PORT
            ),
        mongo_client = MongoClient(
            uri
        )
        _db = mongo_client[DB_NAME]
        _collection = _db[COLLECTION_NAME]
        populate_db(_collection)
    except Exception as exc:
        ("ERROR Mongo init_client: {}".format(exc))
        return None, None
    return mongo_client, _collection


client, default_collection = init_client()
