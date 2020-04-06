def verb_tense_and_inflection(idx,w,sentence,value):
	import sys
	import os
	path=os.path.dirname(os.path.realpath(__file__))
	sys.path.append(path)
	from dep_pos_based_suffix import dep_pos_based_suffix
	import re
	 	
	pa_present_inflection_suffix=[u'am',u'\u0113',u'ed',u'em',u'ed',u'end']
	pa_past_inflection_suffix=[u'ham',u'h\u0113',u'',u'hem',u'hed',u'hend']
	en_pronouns=['I','you','he','she','it','we','you','they']
	pa_pronouns=[u'an', u't\u016b', u'h\u014d', u'am\u0101(h)', u'a\u0161m\u0101(h)', u'hav\u012bn']
	pa_present_perfect_cont_suffix1=[u'h\u0101n',u'h\u0101y',u'h\u0101d',u'h\u0101m',u'h\u0101d',u'h\u0101nd']
	pa_present_perfect_cont_suffix2=[u'estam',u'est\u0113',u'ested',u'estem',u'ested',u'estend']

	
	verb_inflection=[]
	sw=dep_pos_based_suffix(w,idx,sentence)
	print sw,repr(w),idx,repr(sentence)
	
	if sw in [101,102,103,104,105,111,112,113,114,115,150,151,152,153,154,239,240,241,242,243,318,319,320,321,322,323,324,325,326,301,400,401,500,501,502,510,511,603,608,700,701,702,703]:
	
		if len(value['2,3']['def']) != 0:
			
			if value['2,3']['def'][0].endswith('an'):	
				if sw in [101,111,150,239,318,323]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_past_inflection_suffix[0])
				elif sw in [102,112,151,240,319,324]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_past_inflection_suffix[4]) 
				elif sw in [103,113,152,241,320,301,400,401,500,501,511,603,700,702]:
					verb_inflection.append(value['2,3']['def'][0][:-2])
				elif sw in [104,114,153,242,321,325]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_past_inflection_suffix[3])
				elif sw in [105,115,154,243,322,326,502,510,608,701,703]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_past_inflection_suffix[5]) 
				
			elif 'an ' in value['2,3']['def'][0]:
				if sw in [101,111,150,239,318,323]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_past_inflection_suffix[0] + ' ', value['2,3']['def'][0])   )
				elif sw in [102,112,151,240,319,324]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_past_inflection_suffix[4] + ' ', value['2,3']['def'][0])   )  
				elif sw in [103,113,152,241,320,301,400,401,500,501,511,603,700,702]:  
					verb_inflection.append( re.sub(ur'an ',' ', value['2,3']['def'][0])   )
				elif sw in [104,114,153,242,321,325]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_past_inflection_suffix[3] + ' ', value['2,3']['def'][0])   )
				elif sw in [105,115,154,243,322,326,502,510,608,701,703]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_past_inflection_suffix[5] + ' ', value['2,3']['def'][0])   )	
			
		else:
			verb_inflection.append(value['1']['def'][0])
			
	
	elif sw in [100,116,117,118,119,124,125,126,127,155,156,157,158,159,202,227,228,229,230,503,504,505,508,509,602,607,128,129,130,131,132,203,204,205,206,207,254,255,256,257,258,302,303,304,305,306,506,507,604,609,650,651,704,705]:
		if len(value['1']['def']) != 0:
			
			if sw in [116,124,155,227,128,203,254,302]:
				verb_inflection.append(value['1']['def'][0]+ pa_present_inflection_suffix[0])
			elif sw in [117,125,156,228,129,204,255,303]:
				verb_inflection.append(value['1']['def'][0]+ pa_present_inflection_suffix[4])
			elif sw in [100,159,202,503,504,509,602,130,205,256,304,507,604,651,704]:
				verb_inflection.append(value['1']['def'][0]+ pa_present_inflection_suffix[2])
			elif sw in [118,126,157,229,131,206,257,305]:
				verb_inflection.append(value['1']['def'][0]+ pa_present_inflection_suffix[3])
			elif sw in [119,127,158,230,505,508,607,132,207,258,306,506,609,650,705]:
				verb_inflection.append(value['1']['def'][0]+ pa_present_inflection_suffix[5])
			
		else:
			verb_inflection.append(value['2,3']['def'][0])
	
	elif sw in [201,215,216,217,218,264,265,266,267,268,403,404,405,406,407,408,409,410,411,412,601,606,652,653,801,803,805,807]:
	
		if len(value['2,3']['def']) != 0: 
			
			if value['2,3']['def'][0].endswith('an'):	
				if sw in [215,264]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_present_perfect_cont_suffix2[0])
				elif sw in [216,265]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_present_perfect_cont_suffix2[4])  
				elif sw in [201,268,601,653,801,803]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_present_perfect_cont_suffix2[2])
				elif sw in [217,266]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_present_perfect_cont_suffix2[3])
				elif sw in [218,267,606,652,805,807]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+' '+ pa_present_perfect_cont_suffix2[5]) 
				elif sw in [403,408]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [0] + ' ' + value['2,3']['def'][0]) 
				elif sw in [404,409]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [4] + ' ' + value['2,3']['def'][0])
				elif sw in [405,410]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [2] + ' ' + value['2,3']['def'][0]) 
				elif sw in [406,411]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [3] + ' ' + value['2,3']['def'][0])
				elif sw in [407,412]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [5] + ' ' + value['2,3']['def'][0]) 
					
			elif 'an ' in value['2,3']['def'][0]:
				if sw in [215,264]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_present_perfect_cont_suffix2[0] + ' ', value['2,3']['def'][0])   )
				elif sw in [216,265]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_present_perfect_cont_suffix2[4] + ' ', value['2,3']['def'][0])   ) 
				elif sw in [201,268,601,653,801,803]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_present_perfect_cont_suffix2[2] + ' ', value['2,3']['def'][0])   )
				elif sw in [217,266]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_present_perfect_cont_suffix2[3] + ' ', value['2,3']['def'][0])   )
				elif sw in [218,267,606,652,805,807]:
					verb_inflection.append( re.sub(ur'an ',' ' + pa_present_perfect_cont_suffix2[5] + ' ', value['2,3']['def'][0])   )	
				elif sw in [403,408]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [0] + ' ' + value['2,3']['def'][0]) 
				elif sw in [404,409]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [4] + ' ' + value['2,3']['def'][0])
				elif sw in [405,410]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [2] + ' ' + value['2,3']['def'][0]) 
				elif sw in [406,411]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [3] + ' ' + value['2,3']['def'][0])
				elif sw in [407,412]:
					verb_inflection.append('\u0161\u0101y' + pa_present_inflection_suffix [5] + ' ' + value['2,3']['def'][0]) 
			
		else:
			verb_inflection.append(value['1']['def'][0])
			
	elif sw in [269,270,271,272,273,259,260,261,262,263,418,419,420,421,422,600,605,654,655,800,802,804,806]:
		if len(value['2,3']['def']) != 0: 
			
			if value['2,3']['def'][0].endswith('an'):	
				if sw in [269,259,418]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+u' b\u016bd '+ pa_past_inflection_suffix[0])
				elif sw in [270,260,419]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+u' b\u016bd '+ pa_past_inflection_suffix[4])  
				elif sw in [271,261,420,600,655,800,802]:  
					verb_inflection.append(value['2,3']['def'][0][:-2]+u' b\u016bd ')
				elif sw in [272,262,421]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+u' b\u016bd '+ pa_past_inflection_suffix[3])
				elif sw in [273,263,422,605,654,804,806]:
					verb_inflection.append(value['2,3']['def'][0][:-2]+u' b\u016bd '+ pa_past_inflection_suffix[5]) 
				
			elif 'an ' in value['2,3']['def'][0]:
				if sw in [269,259,418]:
					verb_inflection.append( re.sub(ur'an ',u' b\u016bd ' + pa_past_inflection_suffix[0] + ' ', value['2,3']['def'][0])   )
				elif sw in [270,260,419]:
					verb_inflection.append( re.sub(ur'an ',u' b\u016bd ' + pa_past_inflection_suffix[4] + ' ', value['2,3']['def'][0])   )  
				elif sw in [271,261,420,600,655,800,802]: 
					verb_inflection.append( re.sub(ur'an ',u' b\u016bd ', value['2,3']['def'][0])   )
				elif sw in [272,262,421]:
					verb_inflection.append( re.sub(ur'an ',u' b\u016bd ' + pa_past_inflection_suffix[3] + ' ', value['2,3']['def'][0])   )
				elif sw in [273,263,422,605,654,804,806]:
					verb_inflection.append( re.sub(ur'an ',u' b\u016bd ' + pa_past_inflection_suffix[5] + ' ', value['2,3']['def'][0])   )	
			
		else:
			verb_inflection.append(value['1']['def'][0])
	else:
	
		if len(value['2,3']['def']) != 0:
			verb_inflection.append(value['2,3']['def'][0])
		elif len(value['1']['def']) != 0:
			verb_inflection.append(value['1']['def'][0])
	
	return verb_inflection