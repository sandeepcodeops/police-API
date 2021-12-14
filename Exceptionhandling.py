"""
    UK police API data extraction
"""
import requests
import json
import csv
from openpyxl import Workbook
import pandas as pd
import pdfkit
from lxml import html, etree
import logging

logging.basicConfig(filename='logging_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def request_url(url_path):
    """
        got the json format file and status code of the requesting url

    Input:
        :param url_path: input as a url
        :type url_path: url
    Loop:
        :for loop: extracting data inside the json and modifying it
    Return:
        :return : returns the json file
        :rtype : file
    Exception:
        :exception : for error handling like connection, server and some unknown errors

    """
    try:
        logging.info(msg='Response open for fetching data')
        try:
            response = requests.get(url_path).json()
            for data in response:
                data['stop-and-search'] = ",".join(data.get('stop-and-search'))
            logging.debug(response)
        except (ConnectionError, requests.exceptions.HTTPError,
                requests.exceptions.ConnectTimeout) as error:
            logging.error(error)
        try:
            out_file = open("json_output.json", "w")
            json.dump(response, out_file)
            out_file.close()
            logging.info(msg='JSON file is created')
        except (json.JSONDecodeError, OSError) as error:
            logging.error(error)
    except Exception as error:
        logging.error(msg='Some other errors: {}'.format(error))
    finally:
        logging.info(msg='Response closed')


path = 'https://data.police.uk/api/crimes-street-dates'
logging.debug(request_url(path))


def to_csv(file_path):
    """
        This function represents the formation of CSV file from JSON file

    Input:
        :param file_path: input as a json file
        :type file_path: file
    Loop:
        :for loop: extracting data inside the json and modifying it
    Return:
        :return : returns the CSV file
        :rtype : file
    Exception:
        :exception : for error handling like OSError, ValueError  and some unknown errors

    """
    try:
        logging.info(msg='Response open for creating CSV file')
        pd.read_json(file_path).to_csv('csv_output.csv', index=False)
        logging.info(msg='Successfully created a CSV file')
    except (ValueError, OSError) as error:
        logging.error(error)
    except Exception as error:
        logging.error(msg='Some other errors: {}'.format(error))
    finally:
        logging.info(msg='Response closed')


logging.debug(to_csv('my_file.json'))


def csv_xlsx(file_path):
    """
        This function represents the formation of EXCEL file from CSV file

    Input:
        :param file_path: input as a CSV file
        :type file_path: url
    Loop:
        :for loop: extracting data inside the json and modifying it
    Return:
        :return : returns the EXCEL file
        :rtype : file
    Exception:
        :exception : for error handling like OSError, ValueError and some unknown errors

    """
    try:
        logging.info(msg='Response open for creating excel file')
        wb = Workbook()
        ws = wb.active
        try:
            with open(file_path, 'r') as f:
                for row in csv.reader(f):
                    ws.append(row)
        except OSError as error:
            logging.error(error)
        try:
            wb.save('Excel_output.xlsx')
            logging.info(msg='Successfully created excel file')
        except ValueError as error:
            logging.error(error)
    except Exception as error:
        logging.error(msg='Some other errors: {}'.format(error))
    finally:
        logging.info(msg='Response closed')


logging.debug(csv_xlsx('csv_output.csv'))


def csv_html(file_path):
    """
        This function represents the formation of HTML file from CSV file

    Input:
        :param file_path: input as a CSV file
        :type file_path: url
    Loop:
        :for loop: extracting data inside the json and modifying it
    Return:
        :return : returns the HTML file
        :rtype : file
    Exception:
        :exception : for error handling like OSError, ValueError and some unknown errors

    """
    try:
        logging.info(msg='Response open for creating HTML file')
        read_csv = pd.read_csv(file_path)
        try:
            read_csv.to_html("HTML_output.html", index=False)
            read_csv.to_html()
            logging.info(msg='Successfully created HTML file ')
        except ValueError as error:
            logging.error(error)
    except OSError as error:
        logging.error(error)
    except Exception as error:
        logging.error(msg='Some other errors: {}'.format(error))
    finally:
        logging.info(msg='Response closed')


logging.debug(csv_html("csv_output.csv"))


def html_pdf(file_path):
    """
        This function represents the formation of PDF file from HTML file

    Input:
        :param file_path: input as a HTML file
        :type file_path: url
    Loop:
        :for loop: extracting data inside the json and modifying it
    Return:
        :return : returns the PDF file
        :rtype : file
    Exception:
        :exception : for error handling like OSError,IOError, ValueError and some unknown errors

    """
    try:
        logging.info(msg='Response open for creating PDF file')
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        try:
            pdfkit.from_file(file_path, 'PDF_output.pdf', configuration=config)
            logging.info(msg='Successfully created PDF file')
        except ValueError as error:
            logging.error(error)
    except OSError as error:
        logging.error(error)
    except Exception as error:
        logging.error(msg='Some other errors: {}'.format(error))
    finally:
        logging.info(msg='Response closed')


logging.debug(html_pdf('HTML_output.html'))


def html_xml(file_path):
    """
        This function represents the formation of XML file from HTML file

    Input:
        :param file_path: input as a HTML file
        :type file_path: url
    Loop:
        :for loop: extracting data inside the json and modifying it
    Return:
        :return : returns the XML file
        :rtype : file
    Exception:
        :exception : for error handling like OSError,IOError, ValueError and some unknown errors

    """
    try:
        logging.info(msg='Response open for creating XML file')
        with open(file_path, 'r', encoding='utf-8') as inp:
            html_read = html.fromstring(inp.read())
        try:
            with open("xml_output.xml", 'wb') as out:
                out.write(etree.tostring(html_read))
        except ValueError as error:
            logging.error(error)
        logging.info(msg='Successfully created XML file')
    except OSError as error:
        logging.error(error)
    except Exception as error:
        logging.error(msg='Some other errors: {}'.format(error))
    finally:
        logging.info(msg='Response closed')


logging.debug(html_xml("HTML_output.html"))
