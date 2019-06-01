import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        to_js = json.dumps(result)
        return to_js
    return wrapper



@to_json
def get_data():
    return {
        'data': 42
    }

