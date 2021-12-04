from lxml import html, etree

if __name__ == '__main__':

	file = "crime.html"

	with open(file, 'r', encoding='utf-8') as inp:
		htmldoc = html.fromstring(inp.read())

	with open("ukcrime.xml", 'wb') as out:
		out.write(etree.tostring(htmldoc))
