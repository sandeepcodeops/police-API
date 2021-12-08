""" UK police API data extraction"""
import requests
import json
import csv
import logging
logging.basicConfig(filename='logging_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

""" got the json format file and status code of the requesting url"""
response = requests.get('https://data.police.uk/api/crimes-street-dates')
""" HTTP Status Codes: 
    1xx : Informational 
    2xx : Success
    3xx : Redirection
    4xx : Client Error
    5xx : Server Error."""
logging.debug(response.status_code)

json_dict = response.json()


def edit_array(dict1):
    """ This function solve the array in the json_dict

    Input:
        :param dict1: dictionary format input
        :type dict1: dict

    Loop:
        using for loop to edit the data from the dictionary

    Return:
        :return dict1: the updated dictionary
        :rtype dict1: dict
    """
    for data in dict1:
        b = data.get('stop-and-search')
        a = ",".join(b)
        data['stop-and-search'] = a
    return dict1


json_result = edit_array(json_dict)
logging.debug(json_result)


def to_json(para):
    """
    this function represents the json file conversion from a dictionary
    Input:
        :param para: input parameter
        :type para: dict

    Return:
        :return: my_file in json format
        :rtype : file
    """
    out_file = open("my_file.json", "w")

    json.dump(para, out_file)

    out_file.close()


result_jsonfile = to_json(json_dict)
logging.debug(msg='the json file is created')


def to_csv(file_path):
    """ The function represents the conversion of csv file from json

    Input:
        :param file_path: input file in json format
        :type file_path: file

    Body:
        opening a csv file for writing the data
        :loop for extracting each data from the json file and writing the rows in csv format

    Return:
        :return csv_output: returns the csv file as a output
        :rtype : file

    """
    with open(file_path) as json_file:
        """ the CSV file is written from the json file"""
        json_data = json.load(json_file)

    data_file = open('csv_output.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)

    count = 0
    for row in json_data:
        if count == 0:
            header = row.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(row.values())

    data_file.close()


result_csv = to_csv('my_file.json')
logging.debug(msg='the csv file is created')
