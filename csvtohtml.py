import pandas as pd

a = pd.read_csv("jsonoutput.csv")

a.to_html("crime.html", index= False)

html_file = a.to_html()