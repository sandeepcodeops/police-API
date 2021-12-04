import pdfkit

config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_string('crime.html', 'crimePDF.pdf', configuration=config)
