"""
the file formation from csv to html using pandas
"""
import pandas as pd


def csv_html(path):
    """
    this function represents the file convertor

    Input:
        :param path: input is csv file
        :type path: file

    Return:
        :return html_file: returns the crime.html file
        :rtype html_file: file
    """
    read_csv = pd.read_csv(path)

    read_csv.to_html("crime.html", index=False)

    html_file = read_csv.to_html()
    return html_file


csv_html("csv_output.csv")
