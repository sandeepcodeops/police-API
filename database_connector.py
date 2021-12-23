import mysql.connector
import pandas as pd
import logging



csv_data = pd.read_csv('csv_output.csv')
logging.debug(csv_data.head())

try:
    database = mysql.connector.connect(host='localhost', user='sandeep', passwd='1234')
    if database.is_connected():
        cursor = database.cursor()
