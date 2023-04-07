import os

from pymongo.mongo_client import MongoClient


def get_database_connection():
    database_connection_string = os.environ["DATABASE_CONNECTION_STRING"]
    try:
        client = MongoClient(database_connection_string)
        return client
    except Exception as e:
        print(e)


def main(event, context):
    method = event.get("http", {}).get("method", "")
    if method == "POST": 
        get_database_connection()
        return {
            "body": {
                "response": "Success",
            },
            "statusCode": 201,
        }
    return {
        "body": {
            "response": "This method is not supported",
        },
        "statusCode": 401
    }
