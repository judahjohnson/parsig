def lemmatize(lemmatizer,word,pos):
	
	if pos == 'n.' or pos == 'n':
		return lemmatizer.lemmatize(word.lower(),'n')
	elif pos == 'v.' or pos == 'vtr.' or pos == 'vtran.' or pos == 'vintr.' or pos == 'vintran.' or pos == 'intr.' or pos == 'tr.' or pos == 'v':
		return lemmatizer.lemmatize(word.lower(),'v')
	elif pos == 'asj.' or pos == 'adj.' or pos == 'superl.' or pos == 'a':
		return lemmatizer.lemmatize(word.lower(),'a')
	elif pos == 'adv.' or pos == 'r':
		return lemmatizer.lemmatize(word.lower(),'r')
	elif pos == 's':
		return lemmatizer.lemmatize(word.lower(),'s')
		
	else:
		return lemmatizer.lemmatize(word.lower())
		

		
