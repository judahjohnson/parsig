def pdf_to_text(path,p,PDFResourceManager,PDFPageInterpreter,TextConverter,LAParams,PDFPage,StringIO):
	manager = PDFResourceManager()
	retstr = StringIO()
	layout = LAParams(all_texts=True)
	device = TextConverter(manager, retstr, laparams=layout)
	filepath = open(path, 'rb')
	interpreter = PDFPageInterpreter(manager, device)

	for page in PDFPage.get_pages(filepath, pagenos=set([p]), check_extractable=True):
		interpreter.process_page(page)

	text = retstr.getvalue()

	filepath.close()
	device.close()
	retstr.close()
	return text