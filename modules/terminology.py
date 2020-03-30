from __future__ import division
def terminology(terms_path):
	import pandas as pd
	from pandas import ExcelFile
	import sys
	import re

	list=[]
	xl = pd.ExcelFile(terms_path)
	df = xl.parse('Sheet1')
	for i in df.index:
		sys.stdout.write("terminology progress: %f%%   \r" % (100*i/df['a'].count()) )
		sys.stdout.flush()
		if type(df['a'][i]) != float:
			list.append(re.sub(ur'( |-|\u002d|\u005f|\u00ad|\u0331|\u0332|\u0335|\u0336|\u2012|\u2013|\u2014|\u2015|\u2017|\u2212|\u2500)+', '_', df['a'][i].strip(),re.UNICODE).lower())
			
	sys.stdout.write("\n")		
					
	
	return list