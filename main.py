from __future__ import division
import codecs
from nltk import IBMModel2
import sys
import os
import os.path
path=os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
from modules import find_ngrams
from modules import split_sentences
from modules import dict_and_bitext	
from modules import verb_dict	
from modules import synonym_and_bitext
from modules import input_files
from modules import terminology
from modules import convert
from modules import pdf_to_text
from corenlp_pywrap import pywrap
import nltk
from nltk.stem import WordNetLemmatizer
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re
import time
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import resolve1

lemmatizer=WordNetLemmatizer()
path1=os.path.join(path,'stanford-corenlp-full-2017-06-09')
os.system('start cmd /k "cd ' + path1 +' & java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000"') 
path10=os.path.join(path,'unigrams.xlsx')
path11=os.path.join(path,'phrases.xlsx')
path12=os.path.join(path,'verbs.xlsx')
path13=os.path.join(path,'thesaurus.xlsx')

dict1, bitext = dict_and_bitext.dict_and_bitext(lemmatizer,path10,path11)
dict2, bitext = verb_dict.verb_dict(lemmatizer,path12, bitext)
dict1, dict2, bitext = synonym_and_bitext.synonym_and_bitext(dict1,dict2,path13,bitext)

path_list=input_files.input_files(os.path.join(path,'path_list.xlsx'))
start_time = time.time()
for idx1 , d in enumerate(path_list):
	terms_list=terminology.terminology(d['terms_path'])
	if d['path'][-3:].lower() == 'pdf':
		file = open(d['path'], 'rb')
		parser = PDFParser(file)
		document = PDFDocument(parser)
		with codecs.open(d['path'][:-4]+'1.txt', mode='w', encoding='utf-8') as tf1:
			with codecs.open(d['path'][:-4]+'2.txt', mode='w', encoding='utf-8') as tf2:
				for n in range(resolve1(document.catalog['Pages'])['Count']):
					tf1.write('page '+str(n)+'\n')
					tf2.write('page '+str(n)+'\n')
					sentences_list, length = split_sentences.split_sentences(nltk,pdf_to_text.pdf_to_text(d['path'],n,PDFResourceManager,PDFPageInterpreter,TextConverter,LAParams,PDFPage,StringIO))
					for idx3, s in enumerate(sentences_list):
						sys.stdout.write("parsig031520 file %d page %d progress: %f%%   \r" % (idx1,n,100*idx3/length ))
						sys.stdout.flush()
						ent=[]
						pat=[]
						
						##########################
						#s1,l=remove_citations.remove_citations(s)
						#if len(s1) != 0 and len(re.findall(u'[0-9a-zA-Z]',s1)) != 0:				
							#ent, pat, bitext=find_ngrams.find_ngrams(lemmatizer,pywrap,s1,dict1,dict2,terms_list,bitext)	
						###########################
						if len(s) != 0 and len(re.findall(u'[0-9a-zA-Z]',s)) != 0:
							
							ent, pat, bitext=find_ngrams.find_ngrams(lemmatizer,pywrap,s,dict1,dict2,terms_list,bitext)				
						tf1.write(s+'\n')
						#############################
						#ibm1 = IBMModel2(bitext, 5)
						#############################
						tf1.write(' '.join(w+'{'+str(i)+'}' for i,w in enumerate(ent)) + '\n')
						tf1.write(' '.join( '/'.join(w for w in l) +'{'+str(i)+'}' for i,l in enumerate(pat)) + '\n')
						#############################
						#tf2.write(''.join(c for c in l) +' ' + ' '.join(re.sub('_',' ',w,re.UNICODE) for w in pat)+' ')
						#############################
						tf2.write(' '.join(re.sub('_',' ',w[0],re.UNICODE) for w in pat)+' ')
						tf1.write('\n')
					sys.stdout.write("\n")
			
		tf2.close
		tf1.close
		
	elif d['path'][-3:].lower() == 'txt':
		with codecs.open(d['path'], mode='r', encoding='utf-8') as sf:	
			with codecs.open(d['path'][:-4]+'1.txt', mode='w', encoding='utf-8') as tf1:
				with codecs.open(d['path'][:-4]+'2.txt', mode='w', encoding='utf-8') as tf2:
					sentences_list, length = split_sentences.split_sentences(nltk,sf.read())
					for idx3, s in enumerate(sentences_list):
						sys.stdout.write("parsig031520 file %d progress: %f%%   \r" % (idx1,100*idx3/length))
						sys.stdout.flush()
						ent=[]
						pat=[]
						##########################
						#s1,l=remove_citations.remove_citations(s)
						#if len(s1) != 0 and len(re.findall(u'[0-9a-zA-Z]',s1)) != 0:				
							#ent, pat, bitext=find_ngrams.find_ngrams(lemmatizer,pywrap,s1,dict1,dict2,terms_list,bitext)	
						###########################			
						if len(s) != 0 and len(re.findall(u'[0-9a-zA-Z]',s)) != 0:
							ent, pat, bitext=find_ngrams.find_ngrams(lemmatizer,pywrap,s,dict1,dict2,terms_list,bitext)				
						tf1.write(s+'\n')
						###########################
						#ibm1 = IBMModel2(bitext, 5)
						###########################
						tf1.write(' '.join(w+'{'+str(i)+'}' for i,w in enumerate(ent)) + '\n')
						tf1.write(' '.join( '/'.join(w for w in l)  +'{'+str(i)+'}' for i,l in enumerate(pat)) + '\n')
						###########################
						#tf2.write(''.join(c for c in l) +' ' + ' '.join(re.sub('_',' ',w,re.UNICODE) for w in pat)+' ')
						###########################
						tf2.write(' '.join(re.sub('_',' ',w[0],re.UNICODE) for w in pat)+' ')
						tf1.write('\n')
					sys.stdout.write("\n")
				
		tf2.close
		tf1.close
		sf.close

print('time: ', convert.convert(time.time() - start_time))
