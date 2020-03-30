from __future__ import division
def synonym_and_bitext(dictionary1,dictionary2,synonyms_path,bitext):
	import pandas as pd
	from pandas import ExcelFile
	from nltk.translate import AlignedSent, Alignment
	import sys

	xl = pd.ExcelFile(synonyms_path)
	df = xl.parse('Sheet1')
	for i in df.index:
		sys.stdout.write("synonym_and_bitext progress: %f%%   \r" % (100*i/df['a'].count()) )
		sys.stdout.flush()
		if type(df['a'][i]) != float and type(df['b'][i]) != float: 
			if df['b'][i] in dictionary1.keys():
				dictionary1[df['a'][i]]=dictionary1[df['b'][i]]
				for pos in dictionary1[df['b'][i]].keys():
					if len(dictionary1[df['b'][i]][pos]['def']) != 0:
						bitext.append(AlignedSent(dictionary1[df['b'][i]][pos]['def'][0].split(),df['a'][i].split()))
					
			elif df['b'][i] in dictionary2.keys():
				dictionary2[df['a'][i]]=dictionary2[df['b'][i]]
				for pos in dictionary2[df['b'][i]].keys():
					if len(dictionary2[df['b'][i]][pos]['1']['def']) != 0:
						bitext.append(AlignedSent(dictionary2[df['b'][i]][pos]['1']['def'][0].split(),df['a'][i].split()))
					elif len(dictionary2[df['b'][i]][pos]['2,3']['def']) != 0:
						bitext.append(AlignedSent(dictionary2[df['b'][i]][pos]['2,3']['def'][0].split(),df['a'][i].split()))
	sys.stdout.write("\n")		
	return dictionary1, dictionary2, bitext