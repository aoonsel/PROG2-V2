from os.path import join
import uuid
import json

save_file = join('data', 'activities.json')

def save_activity(activity):
    key = str(uuid.uuid4())[:4]

    with open(save_file, 'w+') as file:
        data = json.load(save_file)
        data[key] = activity
        json.dump(data, file, indent=4)
