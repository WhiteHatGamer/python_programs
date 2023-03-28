import json
dict_data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

#dumps every data from dict_data to json_str_file as string with indendation as required
json_str_file = json.dumps(dict_data, indent=4)

#loads the string data in json_str_file as dictionary to decoded_file
decoded_file = json.loads(json_str_file)

#dumping the dictionary in decoded_file which is same as dict_data to the json file present in directory
with open('family_file.json','w') as json_file:
    json.dump(decoded_file,json_file,indent=4)