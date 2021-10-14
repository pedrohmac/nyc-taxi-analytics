import glob2 as glob
import json
import csv

def extract_json(directory):
    keys_list = []
    extracted_data = []
    json_list = []
 
    for json_file in glob.glob(directory + '/*.json'):
        with open(json_file) as infile:
            for line in infile:
                json_list.append(json.loads(line))
            extracted_data = [tuple(value for value in item.values()) for item in json_list]

    keys_list = [key for key in json_list[0].keys()]
    keys_list = ', '.join(keys_list)
    return keys_list, extracted_data


def extract_vendor(file_to_process):
    handler = []
    with open(file_to_process) as infile:
        csv_holder = csv.reader(infile, delimiter=',')
        for i in csv_holder:
            handler.append(i)
        handler[0][0] = 'vendor_id'
        keys_list = ', '.join(handler[0])

        list_handler = []
        for i in handler[1:]:
            csv_dict = dict(zip(handler[0],i))
            list_handler.append(tuple(csv_dict.values()))
    return keys_list, list_handler


def extract_payment(file_to_process):
    handler = []
    with open(file_to_process) as infile:
        csv_holder = csv.reader(infile, delimiter=',')
        for i in csv_holder:
            handler.append(i)
        handler = handler[1:19]

        list_handler = []
        for i in handler[1:]:
            csv_dict = dict(zip(handler[0],i))
            list_handler.append(list(csv_dict.values()))
    return list_handler