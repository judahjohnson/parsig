def split_sentences(nltk,paragraph):
	import re
	
	paragraph=re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', paragraph)
	
	paragraph=re.sub(r'(\\n\\n)+', '. ', paragraph)
	paragraph=re.sub('[.]+', '. ', paragraph)
	paragraph=re.sub('[:]+', '. ', paragraph) 
	paragraph=re.sub('(\s-\s)+', '. ', paragraph)
	paragraph=re.sub('[,]+', ', ', paragraph) 
	paragraph=re.sub('[;]+', '; ', paragraph)

	return nltk.sent_tokenize(paragraph), len(nltk.sent_tokenize(paragraph))