import pandas as pd
from lxml import html, etree


# if __name__ == '__main__':
#
# 	file = "crime.html"


def html_xml(path):
    with open(path, 'r', encoding='utf-8') as inp:
        htmldoc = html.fromstring(inp.read())

    with open("ukcrime.xml", 'wb') as out:
        out.write(etree.tostring(htmldoc))

html_xml("crime.html")
