def word_similarity(word, dictionary1, dictionary2, model):
	
	similarity_dict={}
	for k in set(dictionary1.keys()+dictionary2.keys()):
		try:
			similarity_dict[k]= model.similarity(word, k)
		except KeyError:
			similarity_dict[k]= -1
			pass
	import operator
	return max(similarity_dict.iteritems(), key=operator.itemgetter(1))[0]

import sys
import os
import os.path
path=os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)

from modules import dict_and_bitext	
from modules import verb_dict

path10=os.path.join(path,'unigrams.xlsx')
path11=os.path.join(path,'phrases.xlsx')
path12=os.path.join(path,'verbs.xlsx')


dict1, bitext = dict_and_bitext.dict_and_bitext(lemmatizer,path10,path11)
dict2, bitext = verb_dict.verb_dict(lemmatizer,path12, bitext)

import gensim.downloader as api
model=api.load("fasttext-wiki-news-subwords-300") 


import codecs
ctr1=0	
ctr2=0
fc=[]
sc=[]

# download words_alpha.txt at https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt, and save it inside parsig folder.
path13=os.path.join(path,'words_alpha.txt')

with codecs.open(path13, mode='r', encoding='utf-8') as sf:
	for i, line in enumerate(sf):
		if len(line.split()) == 1:
	
			try :
			
				model.wv[line.strip().lower()]
				print repr(line.strip().lower())
				fc.append(line.strip().lower())
				sc.append(word_similarity(line.strip().lower(), dict1, dict2,model))
				
				ctr1+=1
			except KeyError: 
				try:
					model.wv[line.strip().title()]
					print repr(line.strip().lower())
					fc.append(line.strip().title())
					sc.append(word_similarity(line.strip().title(), dict1, dict2, model))
					ctr1+=1
				
				except:
					try:
						model.wv[line.strip().upper()]
						print repr(line.strip().lower())
						fc.append(line.strip().upper())
						sc.append(word_similarity(line.strip().upper(), dict1, dict2, model))
						ctr1+=1
				
					except:
				
				
						ctr2+=1
						pass
	sf.close
	
import pandas as pd
df = pd.DataFrame({'a': fc ,'b': sc})
path14=os.path.join(path,'thesaurus.xlsx')
writer = pd.ExcelWriter(path14, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
