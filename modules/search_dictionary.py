def search_dictionary(pywrap,lemmatizer,idx,w,s,postl,dict,terminology_list,sw):
	import sys	
	import os
	path=os.path.dirname(os.path.realpath(__file__))
	sys.path.append(path)
	from lemmatize import lemmatize
	if lemmatize(lemmatizer,w,'') in terminology_list:
		return [w]
	else:
		from apostrophe import apostrophe
		
		meaning=[]
		flag=False
		if sw == 'unigram':
			
			if u"'" in w or u"\u2019" in w:
				w=apostrophe(pywrap,w,idx,s,postl)	
			
			w1=lemmatize(lemmatizer,w,postl[idx]['pos'])
			if w1 in dict.keys():
				if len(dict[w1][postl[idx]['pos']]['def']) != 0:
					meaning.extend(dict[w1][postl[idx]['pos']]['def']) 
				else:
					for p in dict[w1].keys():
						if len(dict[w1][p]['def']) != 0:
							meaning.extend(dict[w1][p]['def'])
						
		elif sw == 'verb_ngram': 
			w1=lemmatize(lemmatizer,w,'v.')
			
			#######################################################3
			#if w1 in dict.keys():
			#	if len(dict[w1]['v.']['1']['def']) != 0 or len(dict[w1]['v.']['2,3']['def']) != 0:
			#		meaning.append(verb_tense_and_inflection(idx,w,s,dict[w1]['v.'])[0])
			###########################################################
			
						
			if w1 in dict.keys():
				if len(dict[w1]['v.']['1']['def']) != 0 and len(dict[w1]['v.']['2,3']['def']) == 0:
					meaning.extend(dict[w1]['v.']['1']['def']) 
				elif len(dict[w1]['v.']['1']['def']) == 0 and len(dict[w1]['v.']['2,3']['def']) != 0:
					meaning.extend(dict[w1]['v.']['2,3']['def']) 
				elif len(dict[w1]['v.']['1']['def']) != 0 and len(dict[w1]['v.']['2,3']['def']) != 0:
					meaning.extend(dict[w1]['v.']['1']['def']+dict[w1]['v.']['2,3']['def']) 
					
					
				
		elif sw == 'ngram':
			
			w1=w.lower().strip()					
			if w1 in dict.keys():
				if len(dict[w1]['phrase.']['def']) != 0:
					meaning.extend(dict[w1]['phrase.']['def'])
		
		
		return meaning

