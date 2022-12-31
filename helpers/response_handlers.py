from flask import make_response, jsonify


def create_response(data, status_code=200):
    response = make_response(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status_code = status_code
    return response


def throw_error(error="Something went wrong", status=500, message=None):
    return create_response({"error": {"error": error, "statusCode": status, "message": message}}, status)


def throw_response(data, status=200):
    return create_response({"data": data}, status_code=status)
