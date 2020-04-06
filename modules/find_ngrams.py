def find_ngrams(lemmatizer,pywrap,paragraph,dictionary1,dictionary2,terminology_list,bitext):
	import sys
	import os
	path=os.path.dirname(os.path.realpath(__file__))
	sys.path.append(path)
	from nltk import bigrams
	from nltk import trigrams
	from nltk import ngrams
	from stanford_ner_parser import stanford_ner_parser
	from consecutive_blocks import consecutive_blocks
	from convert_penn_treebank_tagset import convert_penn_treebank_tagset
	from stanford_pos_tagger import stanford_pos_tagger
	from nltk.translate import AlignedSent, Alignment
	from search_dictionary import search_dictionary
	
	
	p,tokens,l=stanford_pos_tagger(pywrap,paragraph)

	unigram_pos_list = convert_penn_treebank_tagset(l)
	
	en_ng_idx_in_dict=[[],[],[],[],[],[],[]] 
	
	pptbts=['MD','VB','VBD','VBG','VBN','VBP','VBZ']
	have_forms=['have','has','had']
	be_forms1=['am','is','are','was','were']
	be_forms2=['be']
	be_forms3=['been']
	be_forms4=['being']
	modals1=['can', 'could', 'may', 'might', 'must', 'shall', 'should', 'will', 'would']
	modals2=['ought','had better','dare','need']
	verb_tense_matrix=[[],[],[],[]] 
	verb_chunks=[]
	for i, d in enumerate(l):
		if d['pos'] in pptbts:
			verb_chunks.append(i)
	
	for b in consecutive_blocks(verb_chunks):
		
		if len(b) == 1:
			verb_tense_matrix[0].extend(b)
		
		elif len(b) == 2:
			if tokens[b[0]] in have_forms:
				verb_tense_matrix[1].extend(b)
			elif tokens[b[0]] in be_forms1:
				verb_tense_matrix[1].extend(b)
			elif tokens[b[0]] in modals1:
				verb_tense_matrix[1].extend(b)
			else:
				verb_tense_matrix[0].extend(b)
		
		elif len(b) == 3:
			if tokens[b[0]] in have_forms and tokens[b[1]] in be_forms3:
				verb_tense_matrix[2].extend(b)
			elif tokens[b[0]] in modals1 and tokens[b[1]] in be_forms2:
				verb_tense_matrix[2].extend(b)
			elif tokens[b[0]] in be_forms1 and tokens[b[1]] in be_forms4:
				verb_tense_matrix[2].extend(b)
			else:
				verb_tense_matrix[0].extend(b)
		
		elif len(b) == 4:
			if tokens[b[0]] in modals1 and tokens[b[1]] in have_forms and tokens[b[2]] in be_forms3:
				verb_tense_matrix[3].extend(b)
			else:
				verb_tense_matrix[0].extend(b)
				
	
	local_dict={}
	
	
	v_ng_idx_in_dict=[]
	for row in verb_tense_matrix:
		for b in consecutive_blocks(row):
			meaning=search_dictionary(pywrap,lemmatizer,b[-1],tokens[b[-1]],paragraph,unigram_pos_list,dictionary2,terminology_list,'verb_ngram')
			for n in range(1,5):
				
				if len(meaning) != 0 and len(b) == n:
					en_ng_idx_in_dict[n-1].extend(b)
					local_dict['_'.join(tokens[i] for i in b)]=meaning
					v_ng_idx_in_dict.extend([i for i in b])
					break
				elif len(meaning) == 0 and len(b) == n:
					bitext.append(AlignedSent('_'.join(tokens[i] for i in b).split(),'_'.join(tokens[i] for i in b).split()))
					break
	
	
	for n in range(2,8)	:
		for j, tup in enumerate(list(ngrams(tokens, n))) :
			meaning=search_dictionary(pywrap,lemmatizer,0,'_'.join(w for i, w in enumerate(tup)),'',[],dictionary1,terminology_list,'ngram')
			if len(meaning) != 0: 
				en_ng_idx_in_dict[n-1].extend(range(j, j + len(tup)))
				local_dict['_'.join(w for i, w in enumerate(tup))]=meaning
			else:
				bitext.append(AlignedSent('_'.join(w for i, w in enumerate(tup)).split(),'_'.join(w for i, w in enumerate(tup)).split()))
	
	for i,t in enumerate(tokens):		
		if i not in v_ng_idx_in_dict:
			meaning=search_dictionary(pywrap,lemmatizer,i,t,paragraph,unigram_pos_list,dictionary1,terminology_list,'unigram')
			if len(meaning) != 0:
				en_ng_idx_in_dict[0].append(i)
				local_dict[t]=meaning
			else:
				bitext.append(AlignedSent(t.split(),t.split()))

	
	m = 7
	while m >= 2:
		for n in range(1,m)	:
			inter=set(en_ng_idx_in_dict[n-1]) & set(en_ng_idx_in_dict[m-1])
			if len(inter) != 0:
				en_ng_idx_in_dict[n-1] = [ i for i in en_ng_idx_in_dict[n-1] if i not in en_ng_idx_in_dict[m-1] ]
				
				for b in consecutive_blocks(en_ng_idx_in_dict[n-1]):
					r= len(b) % n
					if r != 0: 
						en_ng_idx_in_dict[r-1] = sorted(set(en_ng_idx_in_dict[r-1] + [ i for i in en_ng_idx_in_dict[n-1] ])) 
						en_ng_idx_in_dict[r-1] = [ i for i in en_ng_idx_in_dict[r-1] if i not in en_ng_idx_in_dict[m-1] ] 
						en_ng_idx_in_dict[n-1] = [ i for i in en_ng_idx_in_dict[n-1] if i not in en_ng_idx_in_dict[r-1] ]  
											
		m-=1
	
			
	
	ne_ngram_index_matrix=[[],[],[],[],[],[],[]]
	
	if len(p) != 0:
		ne_ngram_index_matrix=stanford_ner_parser(pywrap,p)

	for row in ne_ngram_index_matrix:
		for b in consecutive_blocks(row):
			if len(set(b) & set(en_ng_idx_in_dict[0])) !=0:
				for n in range(2,8):
					if len(b) % n == 0:
						en_ng_idx_in_dict[0] = [i for i in en_ng_idx_in_dict[0] if i not in b]
						en_ng_idx_in_dict[n-1].extend(b)
						en_ng_idx_in_dict[n-1]=sorted(set(en_ng_idx_in_dict[n-1]))	
						break
					
					
	for row in verb_tense_matrix:
		for b in consecutive_blocks(row):
			if len(set(b) & set(en_ng_idx_in_dict[0])) !=0:
				for n in range(2,5):
					if len(b) % n == 0:
						en_ng_idx_in_dict[0] = [i for i in en_ng_idx_in_dict[0] if i not in b]
						en_ng_idx_in_dict[n-1].extend(b)
						en_ng_idx_in_dict[n-1]=sorted(set(en_ng_idx_in_dict[n-1]))	
						break
	
	sentence_recreated=[]
	sentence_recreated_track=[]
	for i in range(len(tokens)):
		sentence_recreated.append('')
		
	for j in en_ng_idx_in_dict[0]:
		sentence_recreated[j]=tokens[j]
		sentence_recreated_track.append(j)
	
	for n in range(1,7)	: 
		for b in consecutive_blocks(en_ng_idx_in_dict[n]):	
			sentence_recreated[b[0]]='_'.join(tokens[j] for j in b)
			sentence_recreated_track.extend(j for j in b)
	
	
	for j in [i for i in range(len(tokens)) if i not in sorted(sentence_recreated_track)] :
		sentence_recreated[j]=tokens[j]

	en_sentence=[]
	for w in sentence_recreated:
		if len(w.strip()) != 0:
		 en_sentence.append(w)
	
	pa_sentence=[]
	for w in en_sentence:
		if w in local_dict:
			pa_sentence.append(local_dict[w])
		else:
			pa_sentence.append([w])
	
	return en_sentence, pa_sentence, bitext