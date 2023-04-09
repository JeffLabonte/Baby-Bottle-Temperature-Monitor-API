import os
from datetime import datetime

from pymongo.mongo_client import MongoClient


def get_database_connection() -> MongoClient:
    database_connection_string = os.environ["DATABASE_CONNECTION_STRING"]
    try:
        return MongoClient(database_connection_string)
    except Exception as e:
        raise e


def insert_temperature(temperature_in_celcius):
    client = get_database_connection()
    temperature_data = {
        "temperature_in_celcius": temperature_in_celcius,
        "recorded_at": datetime.now(),
    }
    database = client.baby_bottle
    temperature_collection = database.temperature
    temperature_collection.insert_one(temperature_data)


def handle_post(event, _):
    try:
        temperature = event.get("temperature_in_celcius")
        if float(temperature):
            insert_temperature(temperature)
            return {
                "body": {
                    "response": "Success",
                },
                "statusCode": 201,
            }
    except ValueError:
        print("Unable to convert temperature to float")

    return {
        "statusCode": 400,
    }


def handle_get():
    client = get_database_connection()
    database = client.baby_bottle
    temperature_collection = database.temperature
    temperature = temperature_collection.find().sort("recorded_at", -1).limit(1)
    return {
        "body": {
            "temperature": float(temperature[0].get("temperature_in_celcius", 0)),
        },
        "statusCode": 200,
    }


def main(event, context):
    method = event.get("http", {}).get("method", "")
    if method == "POST":
        return handle_post(event, context)

    if method == "GET":
        return handle_get()

    return {
        "body": {
            "response": "This method is not supported",
        },
        "statusCode": 401,
    }


if __name__ == "__main__":
    """
    Can be used for local testing
    """
    pass
