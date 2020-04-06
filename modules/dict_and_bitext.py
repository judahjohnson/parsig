from __future__ import division
def dict_and_bitext(lemmatizer,unigrams_path,phrases_path):
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
	bitext = []
	tl=[]
	
	xl = pd.ExcelFile(unigrams_path)
	df = xl.parse('Sheet1')
	for i in df.index:
		sys.stdout.write("dict_and_bitext unigrams progress: %f%%   \r" % (100*i/df['a'].count()) )
		sys.stdout.flush()
		if type(df['a'][i]) != float and type(df['b'][i]) != float and type(df['c'][i]) != float:
			bitext.append(AlignedSent(df['c'][i].split(),df['a'][i].split()))
			t=(lemmatize(lemmatizer,re.sub('( |-|\u002d|\u005f|\u00ad|\u0331|\u0332|\u0335|\u0336|\u2012|\u2013|\u2014|\u2015|\u2017|\u2212|\u2500)+', '_', df['a'][i]).strip(),df['b'][i].strip()), df['b'][i].strip(), 'def', df['c'][i].strip())
			tl.append(t)
		
	sys.stdout.write("\n")		
					
	
	xl = pd.ExcelFile(phrases_path)
	df = xl.parse('Sheet1')
	for i in df.index:
		sys.stdout.write("dict_and_bitext phrases progress: %f%%   \r" % (100*i/df['a'].count()) )
		sys.stdout.flush()
		if type(df['a'][i]) != float and type(df['c'][i]) != float:
			bitext.append(AlignedSent(df['c'][i].split(),df['a'][i].split()))
			t=(lemmatize(lemmatizer,re.sub('( |-|\u002d|\u005f|\u00ad|\u0331|\u0332|\u0335|\u0336|\u2012|\u2013|\u2014|\u2015|\u2017|\u2212|\u2500)+', '_', df['a'][i]).strip(),'phrase.'), 'phrase.', 'def', df['c'][i].strip())
			tl.append(t) 
	sys.stdout.write("\n")					
	dict=defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
	tl=list(set(tl))
	for x,y,z,v in tl:
		dict[x][y][z].append(v)
	return dict, bitext