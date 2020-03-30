def word_sense_disambiguation(ambiguous_word,sense1,sense2,tokens,model):
	import numpy as np
	import sys
	import os
	path=os.path.dirname(os.path.realpath(__file__))
	sys.path.append(path)
	from vector_similarity import vector_similarity
	s=np.zeros(300)
	
	ctr=0
	for t in tokens:
		if t != ambiguous_word:
			try:
				s=np.add(s,model.wv[t])
				ctr+=1
			except KeyError: 
				try: 
					s=np.add(s,model.wv[t.lower()])
					ctr+=1
				except KeyError:
					try:
						s=np.add(s,model.wv[t.capitalize()])
						ctr+=1
					except KeyError: 
						try:
							s=np.add(s,model.wv[t.upper()])
							ctr+=1
						except KeyError:
							pass		
	if ctr != 0:
		centroid=s/ctr
	else: 
		centroid=np.zeros(300)
			
	if 	vector_similarity(centroid, model.wv[sense1])	>= vector_similarity(centroid, model.wv[sense2]):
		return sense1
	else:
		return sense2