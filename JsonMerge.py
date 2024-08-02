# JsonMerge.py
import json, glob

def merge_json(name_pattern):
    file_list = glob.glob(f'{name_pattern}*')

    solved_list = []
    for file in file_list:
        with open(file) as f:
            solved_list.append(json.load(f))

    file_name = f'{name_pattern}List.json'
    with open(file_name, 'w') as f:
        json.dump(solved_list, f)

    return file_name