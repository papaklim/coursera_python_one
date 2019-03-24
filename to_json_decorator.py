import json


def to_json(func):
    def wrapper():
        result = func()
        to_js = json.dumps(result)
        return to_js
    return wrapper


@to_json
def get_data():
    return {
        'data': 42
    }

