"""
    UK police API data extraction
"""

import requests
import json
import pandas as pd
import pdfkit
import logging

logging.basicConfig(filename='logging_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class UKPoliceAPI:
    """
    the class represents the blueprint functions

    :param: url, json file, csv file, html file

    """
    def __init__(self, url_path, file_path, csv_file_path, html_file_path):
        self.url_path = url_path
        self.file_path = file_path
        self.csv_file_path = csv_file_path
        self.csv_dataframe = pd.read_csv(self.csv_file_path)
        self.html_file_path = html_file_path

    def request_url(self):
        """
            got the json format file and status code of the requesting url

        Input:
            :param : input as a url and file
            :type : url, file
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
                response = requests.get(self.url_path).json()
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

    def json_to_csv(self):
        try:
            logging.info(msg='Response open for creating CSV file')
            pd.read_json(self.file_path).to_csv('csv_output.csv', index=False)
            logging.info(msg='Successfully created a CSV file')
        except (ValueError, OSError) as error:
            logging.error(error)
        except Exception as error:
            logging.error(msg='Some other errors: {}'.format(error))
        finally:
            logging.info(msg='Response closed')

    def csv_to_excel(self):
        try:
            logging.info(msg='Response started to create the excel file')
            excel_writer = pd.ExcelWriter('Excel_output.xlsx')
            self.csv_dataframe.to_excel(excel_writer, index=False)
            excel_writer.save()
            logging.info(msg='the excel file is created')
        except ValueError as error:
            logging.error(error)
        except Exception as error:
            logging.error(error)
        finally:
            logging.info(msg='Response is closed')

    def csv_to_html(self):
        try:
            logging.info(msg='Response started to create the html file')
            self.csv_dataframe.to_html("HTML_output.html", index=False)
            self.csv_dataframe.to_html()
            logging.info(msg='the html file is created')
        except ValueError as error:
            logging.error(error)
        except Exception as error:
            logging.error(error)
        finally:
            logging.info(msg='Response is closed')

    def csv_to_xml(self):
        try:
            logging.info(msg='Response started to create the xml file')
            self.csv_dataframe.to_xml('xml_output.xml')
            logging.info(msg='the xml file is created')
        except ValueError as error:
            logging.error(error)
        except Exception as error:
            logging.error(error)
        finally:
            logging.info(msg='Response is closed')

    def html_to_pdf(self):
        try:
            logging.info(msg='Response started to create the pdf file')
            config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
            pdfkit.from_file(self.html_file_path, 'PDF_output.pdf', configuration=config)
            logging.info(msg='the pdf file is created')
        except (OSError, ValueError) as error:
            logging.error(error)
        except Exception as error:
            logging.error(error)
        finally:
            logging.info(msg='Response is closed')


path = 'https://data.police.uk/api/crimes-street-dates'
json_file_path = 'json_output.json'
csv_file = 'csv_output.csv'
html_file = "HTML_output.html"
object_for_class = UKPoliceAPI(url_path=path, file_path=json_file_path, csv_file_path=csv_file, html_file_path=html_file)
logging.debug(object_for_class.request_url())
logging.debug(object_for_class.json_to_csv())
logging.debug(object_for_class.csv_to_xml())
logging.debug(object_for_class.csv_to_excel())
logging.debug(object_for_class.csv_to_html())
logging.debug(object_for_class.html_to_pdf())
