import json
import pandas as pd
import openai
from tqdm import tqdm
import re
from datasets import load_dataset



# Load JSON data from file
with open('.../dataset_spatial/SPARTUN/test_simple.json', 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4, sort_keys=True)) 
    #json.dumps() method to format the JSON data neatly. This method converts the JSON object into a formatted string which is then easy to print.

def find_keys(json_object, path='', keys_set=None):
    if keys_set is None:
        keys_set = set()
    
    if isinstance(json_object, dict):
        for key, value in json_object.items():
            # Construct a path to the key
            new_path = f"{path}.{key}" if path else key
            keys_set.add(new_path)
            find_keys(value, new_path, keys_set)
    elif isinstance(json_object, list):
        for item in json_object:
            find_keys(item, path, keys_set)

    return keys_set

    # Find all unique keys
unique_keys = find_keys(data)

    # Print all unique keys
for key in sorted(unique_keys):
    print(key)
    
    
with open('../dataset_spatial/spartqa_yn/spartqa_YN_test.jsonl', 'r') as file:
    examples = []
    for line in file:
        spartYN = json.loads(line)  # Parse the JSON data from each line
    
        story = spartYN['story']  # Directly access the 'story' string
        question = spartYN['question']  # Directly access the 'question' string
        true_answer = spartYN['answer'].strip()  # Access and strip the 'answer' string
        example=[story,question,true_answer]
        examples.append(example)
                
print(examples[:5])
