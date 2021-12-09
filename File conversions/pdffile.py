"""
the file conversion from html to PDF
"""
import pdfkit


def html_pdf(path):
    """
    Input:
        :param path: input is html file
        :type path: file

    Return:
        :return: PDF file
        :rtype: file
    """
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    result = pdfkit.from_file(path, 'crimePDF.pdf', configuration=config)
    return result


html_pdf('crime.html')
