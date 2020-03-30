def stanford_ner_parser(pywrap,sentence):
	import sys
	import os
	path=os.path.dirname(os.path.realpath(__file__))
	sys.path.append(path)
	from consecutive_blocks import consecutive_blocks

	cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=["ner"])
	out = cn.basic(sentence.encode('utf-8'), out_format='json')
	
	index_list=[]
	for i, e in enumerate(out.json()['sentences'][0]['tokens']):
	
		if e['ner'] != 'O': 
			index_list.append(i)
	
	consecutive_blocks(index_list)

	ngram_index_matrix=[[],[],[],[],[],[],[]]
	
	for b in consecutive_blocks(index_list):
		for n in range(1,8):
			if len(b) == n:	
				ngram_index_matrix[n-1].extend(b)
		
		
	return ngram_index_matrix