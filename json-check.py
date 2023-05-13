import json
import os

def check_json(directory):
    example_json_string = '''{
        "english": {
            "word": "",
            "examples": [],
            "gender": [],
            "trick-words": []
        },
        "portuguese": {
            "word": "",
            "examples": [],
            "gender": [],
            "trick-words": []
        },
        "progress": {
            "memory": 0.0,
            "gender-memory": 0.0
        },
        "type": [],
        "dates": {
            "discover-date": "",
            "next-review": "",
            "last-reviewed": ""
        },
        "synotics": {
            "funny": {
                "user-made": [],
                "suggested": []
            },
            "sad": {
                "user-made": [],
                "suggested": []
            },
            "angry": {
                "user-made": [],
                "suggested": []
            },
            "surprising": {
                "user-made": [],
                "suggested": []
            },
            "smell": {
                "user-made": [],
                "suggested": []
            },
            "touch": {
                "user-made": [],
                "suggested": []
            },
            "connection": {
                "user-made": [],
                "suggested": []
            }
        }
    }'''

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                try:
                    data = json.load(f)
                    if data.keys() != json.loads(example_json_string).keys():
                        print(f'Error: {filename} does not have the same keys as the example json file')
                    else:
                        for key in data.keys():
                            if type(data[key]) != type(json.loads(example_json_string)[key]):
                                if(key != 'type'):
                                    print(f'Error: {filename} has a different type for key "{key}"')
                            elif isinstance(data[key], dict):
                                if data[key].keys() != json.loads(example_json_string)[key].keys():
                                    print(f'Error: {filename} does not have the same keys for key "{key}"')
                except ValueError as e:
                    print(f'Error: {filename} is not valid json. Details: {e}')

check_json('./tmp')
