from file_converter import converter_functions

path = 'https://data.police.uk/api/crimes-street-dates'
json_file_path = 'json_output.json'
csv_file = 'csv_output.csv'
html_file = "HTML_output.html"
converter_functions.request_url(url_path=path)
