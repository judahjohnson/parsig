def remove_citations(sentence):
	import re		
	return re.sub(u'\[[0-9]+\]','',sentence), re.findall(u'\[[0-9]+\]',sentence)
	