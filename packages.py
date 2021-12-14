from uk_police import uk_police_package

path = 'https://data.police.uk/api/crimes-street-dates'
# json_file_path = 'json_output.json'
# csv_file = 'csv_output.csv'
# html_file = "HTML_output.html"
obj = uk_police_package.UKPoliceAPI(url_path=path)
obj.request_url()
