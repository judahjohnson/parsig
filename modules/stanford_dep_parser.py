def stanford_dep_parser(pywrap,w,idx,sentence):
	cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=["depparse"])
	out = cn.basic(sentence.encode('utf-8'), out_format='json')

	flag=False
	for e in out.json()['sentences'][0]['basicDependencies']:
		if e['dep'] == 'cop' and not flag:
			if e['governorGloss'] == w and e['governor'] == idx+1: 
				flag=True
			elif e['dependentGloss'] == w  and e['dependent'] == idx+1:		
				flag=True
							
	return flag