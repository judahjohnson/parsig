def stanford_pos_tagger(pywrap,paragraph):
	
	cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=["pos"])
	out = cn.basic(paragraph, out_format='json')
		
	list=[]
	tokens=[]
	for d in out.json()['sentences'][0]['tokens']:
		dict={'word': d['word'], 'pos': d['pos']}
		list.append(dict)
		tokens.append(d['word'])
	return ' '.join(w for w in tokens).strip(), tokens, list