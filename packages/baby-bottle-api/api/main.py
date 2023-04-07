def main(event, context):
    print(event)
    method = event.get("http", {}).get("method", "")
    if method == "POST": 
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
