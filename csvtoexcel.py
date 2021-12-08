"""
The script contains the formation of xlsx file from csv file
"""
from openpyxl import Workbook
import csv

wb = Workbook()
ws = wb.active


def csv_xlsx(path):
    """
    this function represents the xlsx file formation

    Input:
        :param path: input file of csv file
        :type path: file
    Return:
        :return: xlsx file will returns
        :rtype: file
    """
    with open(path, 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    result = wb.save('csvtoxl.xlsx')
    return result


csv_xlsx('csv_output.csv')
