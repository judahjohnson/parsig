def verb_dict(lemmatizer,unigrams_path,bitext):
	import pandas as pd
	from pandas import ExcelFile
	from nltk.translate import AlignedSent, Alignment
	import sys
	import os
	path=os.path.dirname(os.path.realpath(__file__))
	sys.path.append(path)
	from lemmatize import lemmatize
	import re
	from collections import defaultdict	
	
	dict={}
	tl=[]
	 
	xl = pd.ExcelFile(unigrams_path)
	df = xl.parse('Sheet1')
	for i in df.index:
		sys.stdout.write("verb_dict unigrams progress: %f%%   \r" % (100*i/df['a'].count()) )
		sys.stdout.flush()
		if type(df['a'][i]) != float and type(df['c'][i]) != float and type(df['d'][i]) != float:
			bitext.append(AlignedSent(df['c'][i].split(),df['a'][i].split()))
			t=(lemmatize(lemmatizer,re.sub('( |-|\u002d|\u005f|\u00ad|\u0331|\u0332|\u0335|\u0336|\u2012|\u2013|\u2014|\u2015|\u2017|\u2212|\u2500)+', '_', df['a'][i]).strip(),'v.'), 'v.', str(df['d'][i]).strip(), 'def', df['c'][i].strip())
			tl.append(t)
		
	sys.stdout.write("\n")		
	dict=defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
	tl=list(set(tl))
	for w,x,y,z,v in tl:
		dict[w][x][y][z].append(v)
	return dict, bitext