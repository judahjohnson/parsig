def apostrophe(pywrap,w,idx,sentence,postl):
	import sys
	import os
	path=os.path.dirname(os.path.realpath(__file__))
	sys.path.append(path)
	from stanford_dep_parser import stanford_dep_parser 
	import re
	
	
	if re.search(u"\u2019s|'s", w) == None:
		return w.replace(u'\u2019ll','will').replace(u'\u2019m','am').replace(u'\u2019ve','have').replace(u'\u2019re','are').replace(u'n\u2019t','not').replace(u's\u2019','s').replace(u"'ll",'will').replace(u"'m",'am').replace(u"'ve",'have').replace(u"'re",'are').replace(u"n't",'not').replace(u"s'",'s')
	else:
		if idx < len(postl) - 1:
			if postl[idx+1]['penn_pos'] == 'VBN':
				return w.replace(u'\u2019s','has').replace(u"'s",'has')
			elif postl[idx+1]['penn_pos'] == 'VBG':
				return w.replace(u'\u2019s','is').replace(u"'s",'is')
			elif postl[idx+1]['penn_pos'] == 'RB': 
				if idx < len(postl) - 2: 
					if postl[idx+2]['penn_pos'] == 'VBN':
						return w.replace(u'\u2019s','has').replace(u"'s",'has')
					elif postl[idx+2]['penn_pos'] == 'VBG':
						return w.replace(u'\u2019s','is').replace(u"'s",'is')
					else:
						return w.replace(u'\u2019s','s').replace(u"'s",'s')
				else: 
					return w.replace(u'\u2019s','s').replace(u"'s",'s')
			elif stanford_dep_parser(pywrap,w.replace(u's\u2019',"'s"),idx,sentence.replace(u's\u2019',"'s")):#he's really good
				return w.replace(u'\u2019s','is').replace(u"'s",'is')
			
			elif idx > 0: 
				if postl[idx-1]['word'].lower() == 'let':
					return w.replace(u'\u2019s','us').replace(u"'s",'us')	
				else:
				
					return w.replace(u'\u2019s','s').replace(u"'s",'s')
		elif idx == len(postl) - 1: 
			return w.replace(u'\u2019s','s').replace(u"'s",'s') 
