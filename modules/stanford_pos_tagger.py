def stanford_pos_tagger(pywrap,paragraph):
	
	import string
	import re
	
	paragraph=re.sub(ur'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', paragraph,re.UNICODE)
	
	paragraph=re.sub(ur'(\\n\\n)+', '. ', paragraph,re.UNICODE) 
	paragraph=re.sub(ur"(@[A-Za-z0-9_]+)"," ",paragraph,re.UNICODE)
	paragraph=re.sub(ur'_|-|\u002d|\u005f|\u00ad|\u0331|\u0332|\u0335|\u0336|\u2012|\u2013|\u2014|\u2015|\u2017|\u2212|\u2500', ' ', paragraph,re.UNICODE)
	
	paragraph=re.sub(ur'%', ur'% ', paragraph,re.UNICODE)
	paragraph=re.sub(ur'%  +', ur'% ', paragraph,re.UNICODE)
	

	cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=["pos"])
	out = cn.basic(paragraph.encode('utf-8'), out_format='json')
		
	list=[]
	tokens=[]
	for d in out.json()['sentences'][0]['tokens']:
		dict={'word': d['word'], 'pos': d['pos']}
		list.append(dict)
		tokens.append(d['word'])
	return ' '.join(w for w in tokens).strip(), tokens, list