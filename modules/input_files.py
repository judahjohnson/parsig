from __future__ import division
def input_files(path):
	import pandas as pd
	from pandas import ExcelFile
	import sys
	import re
	
	list=[]
	
	xl = pd.ExcelFile(path)
	df = xl.parse('Sheet1')
	for i in df.index:
		sys.stdout.write("input_files progress: %f%%   \r" % (100*i/df['a'].count()) )
		sys.stdout.flush()
		if type(df['a'][i]) != float and type(df['b'][i]) != float:
			d={'path':df['a'][i],'terms_path':df['b'][i]}
			list.append(d)
			
		
	sys.stdout.write("\n")		
				
	
	return list