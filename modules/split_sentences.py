def split_sentences(nltk,paragraph):
	import re
	import string
	
	paragraph=re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', paragraph)
	paragraph=re.sub(r'(\\n\\n)+', '. ', paragraph)
	paragraph=re.sub('[.]+', '. ', paragraph)
	paragraph=re.sub('[:]+', '. ', paragraph) 
	paragraph=re.sub('(\s-\s)+', '. ', paragraph)
	paragraph=re.sub('[,]+', ', ', paragraph) 
	paragraph=re.sub('[;]+', '; ', paragraph)
	paragraph=re.sub("\u2032|\u2019", "'", paragraph)
	paragraph=re.sub('(\\n\\n)+', '. ', paragraph) 
	paragraph=re.sub("(@[A-Za-z0-9_]+)"," ",paragraph)
	paragraph=re.sub('_|-|\u002d|\u005f|\u00ad|\u0331|\u0332|\u0335|\u0336|\u2012|\u2013|\u2014|\u2015|\u2017|\u2212|\u2500', ' ', paragraph)
	paragraph=re.sub('%', '% ', paragraph)
	paragraph=re.sub('%  +', '% ', paragraph)
	paragraph=re.sub('ﬁ', "fi", paragraph)
	paragraph=re.sub('ﬀ', "ff", paragraph)
	paragraph=re.sub('ﬂ', "fl", paragraph)
	paragraph=re.sub('ﬃ', "ffi", paragraph)
	paragraph=re.sub('ﬄ', "ffl", paragraph)
	paragraph=re.sub('ﬅ', "ft", paragraph)
	
	printable = set(string.printable)
	
	return nltk.sent_tokenize(''.join(filter(lambda x: x in printable, paragraph))), len(nltk.sent_tokenize(''.join(filter(lambda x: x in printable, paragraph))))
