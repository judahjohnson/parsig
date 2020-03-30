def dep_pos_based_suffix(pywrap,nltk,verb,idx,sentence):
	cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=["depparse","pos"])
	out = cn.basic(sentence.encode('utf-8'), out_format='json')
	
	sw=0
	dil1=find_dependent(out.json()['sentences'][0]['basicDependencies'],'nsubj',verb,idx+1) 
	dil2=find_dependent(out.json()['sentences'][0]['basicDependencies'],'aux',verb,idx+1) 
	dil3=find_dependent(out.json()['sentences'][0]['basicDependencies'],'auxpass',verb,idx+1) 
	dil4=find_dependent(out.json()['sentences'][0]['basicDependencies'],'nsubjpass',verb,idx+1) 
	dil5=find_dependent(out.json()['sentences'][0]['basicDependencies'],'cop',verb,idx+1)
	dil6=[]
	if len(dil5) == 1:
		dil6=find_dependent(out.json()['sentences'][0]['basicDependencies'],'nsubj',dil5[0]['word'],dil5[0]['idx'])
	
	
	p1=find_pos(out.json()['sentences'][0]['tokens'],{'word':verb,'idx':idx+1}) 
	if len(dil1) == 1 and len(dil4) ==0: 
		p2=find_pos(out.json()['sentences'][0]['tokens'],dil1[0]) 
	if len(dil1) == 0 and len(dil4) ==1:
		p2=find_pos(out.json()['sentences'][0]['tokens'],dil4[0]) 
	if len(dil1) == 0 and len(dil4) ==0 and len(dil6) == 1:
		p2=find_pos(out.json()['sentences'][0]['tokens'],dil6[0])
	if len(dil2) == 1:
		p3=find_pos(out.json()['sentences'][0]['tokens'],dil2[0]) 
	if len(dil2) == 2 and len(dil3) == 0: 
		p4=find_pos(out.json()['sentences'][0]['tokens'],dil2[0]) 
		p5=find_pos(out.json()['sentences'][0]['tokens'],dil2[1]) 
	if len(dil2) == 3 and len(dil3) == 0:
		p6=find_pos(out.json()['sentences'][0]['tokens'],dil2[0])
		p7=find_pos(out.json()['sentences'][0]['tokens'],dil2[1])
		p8=find_pos(out.json()['sentences'][0]['tokens'],dil2[2])
	if len(dil2) == 2 and len(dil3) == 1: 
		p6=find_pos(out.json()['sentences'][0]['tokens'],dil2[0]) 
		p7=find_pos(out.json()['sentences'][0]['tokens'],dil2[1]) 
		p8=find_pos(out.json()['sentences'][0]['tokens'],dil3[0]) 
	if len(dil3) == 1:
		p9=find_pos(out.json()['sentences'][0]['tokens'],dil3[0]) 	

		
	en_pronouns=['I','you','he','she','it','we','you','they']
	if len(dil1) == 1 or len(dil4) == 1 or len(dil6) == 1: 
		if p2 == 'PRP':		
			
			if len(dil2) == 0 and len(dil3) == 0:						
				if p1 == 'VBZ':
					sw=100						
				elif p1 == 'VBD':
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]: 
							sw=101
						elif dil1[0]['word'] == en_pronouns[1]: 
							sw=102
						elif dil1[0]['word'] in en_pronouns[2:5]: 
							sw=103
						elif dil1[0]['word'] == en_pronouns[5]: 
							sw=104
						elif dil1[0]['word'] == en_pronouns[7]: 
							sw=105
					
					elif len(dil4) == 1:
						if dil4[0]['word'] == en_pronouns[0]: 
							sw=106
						elif dil4[0]['word'] == en_pronouns[1]: 
							sw=107
						elif dil4[0]['word'] in en_pronouns[2:5]: 
							sw=108
						elif dil4[0]['word'] == en_pronouns[5]: 
							sw=109
						elif dil4[0]['word'] == en_pronouns[7]: 
							sw=110
					
					elif len(dil6) == 1: 
						if dil6[0]['word'] == en_pronouns[0]: 
							sw=111
						elif dil6[0]['word'] == en_pronouns[1]: 
							sw=112
						elif dil6[0]['word'] in en_pronouns[2:5]: 
							sw=113
						elif dil6[0]['word'] == en_pronouns[5]: 
							sw=114
						elif dil6[0]['word'] == en_pronouns[7]: 
							sw=115	
						
						
						
				elif p1 == 'VBP':
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]: 
							sw=116
						elif dil1[0]['word'] == en_pronouns[1]: 
							sw=117
						elif dil1[0]['word'] == en_pronouns[5]: 
							sw=118
						elif dil1[0]['word'] == en_pronouns[7]: 
							sw=119
					
					elif len(dil4) == 1:					
						if dil4[0]['word'] == en_pronouns[0]: 
							sw=120
						elif dil4[0]['word'] == en_pronouns[1]: 
							sw=121
						elif dil4[0]['word'] == en_pronouns[5]: 
							sw=122
						elif dil4[0]['word'] == en_pronouns[7]: 
							sw=123
					
					elif len(dil6) == 1: 	
						if dil6[0]['word'] == en_pronouns[0]: 
							sw=124
						elif dil6[0]['word'] == en_pronouns[1]: 
							sw=125
						elif dil6[0]['word'] == en_pronouns[5]: 
							sw=126
						elif dil6[0]['word'] == en_pronouns[7]: 
							sw=127
				elif p1 == 'VB':
					if len(dil6) == 1: 	
						if dil6[0]['word'] == en_pronouns[0]: 
							sw=128
						elif dil6[0]['word'] == en_pronouns[1]: 
							sw=129
						elif dil6[0]['word'] in en_pronouns[2:5]: 
							sw=130
						elif dil6[0]['word'] == en_pronouns[5]: 
							sw=131
						elif dil6[0]['word'] == en_pronouns[7]: 
							sw=132
				
			elif len(dil2) == 0 and len(dil3) == 1:
				
				if p9 == 'VBD' and p1 == 'VBN':
					if len(dil4) == 1: 
						if dil4[0]['word'] == en_pronouns[0]: 
							sw=150
						elif dil4[0]['word'] == en_pronouns[1]: 
							sw=151
						elif dil4[0]['word'] in en_pronouns[2:5]: 
							sw=152
						elif dil4[0]['word'] == en_pronouns[5]: 
							sw=153
						elif dil4[0]['word'] == en_pronouns[7]: 
							sw=154
							
				elif p9 == 'VBP' and p1 == 'VBN':
					if len(dil4) == 1: 
						if dil4[0]['word'] == en_pronouns[0]: 
							sw=155
						elif dil4[0]['word'] == en_pronouns[1]: 
							sw=156
						elif dil4[0]['word'] == en_pronouns[5]: 
							sw=157
						elif dil4[0]['word'] == en_pronouns[7]: 
							sw=158
				elif p9 == 'VBZ' and p1 == 'VBN':  is defeated
					if len(dil4) == 1: 
						if dil4[0]['word'] in en_pronouns[2:5]: 
							sw=159
				
			elif len(dil2) == 1 and len(dil3) == 0:
				if p3 == 'VBD' and p1 == 'VBN': 
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]:
							sw=269
						elif dil1[0]['word'] == en_pronouns[1]:
							sw=270
						elif dil1[0]['word'] in en_pronouns[2:5]:
							sw=271
						elif dil1[0]['word'] == en_pronouns[5]:
							sw=272
						elif dil1[0]['word'] == en_pronouns[7]:
							sw=273
				elif p3 == 'VBZ' and p1 == 'VBN': 
					sw=201
				elif p3 == 'VBZ' and p1 == 'VBG': 
					sw=202
				elif p3 == 'MD' and p1 == 'VB': 
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]:
							sw=203
						elif dil1[0]['word'] == en_pronouns[1]:
							sw=204
						elif dil1[0]['word'] in en_pronouns[2:5]:
							sw=205
						elif dil1[0]['word'] == en_pronouns[5]:
							sw=206
						elif dil1[0]['word'] == en_pronouns[7]:
							sw=207
					elif len(dil4) == 1:	
						if dil4[0]['word'] == en_pronouns[0]:
							sw=208
						elif dil4[0]['word'] == en_pronouns[1]:
							sw=209
						elif dil4[0]['word'] in en_pronouns[2:5]:
							sw=210
						elif dil4[0]['word'] == en_pronouns[5]:
							sw=211
						elif dil4[0]['word'] == en_pronouns[7]:
							sw=212
					elif len(dil6) == 1:	
						if dil6[0]['word'] == en_pronouns[0]:
							sw=213
						elif dil6[0]['word'] == en_pronouns[1]:
							sw=214
						elif dil6[0]['word'] in en_pronouns[2:5]:
							sw=215
						elif dil6[0]['word'] == en_pronouns[5]:
							sw=216
						elif dil6[0]['word'] == en_pronouns[7]:
							sw=217
					
					
				elif p3 == 'VBP' and p1 == 'VBN': 
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]: 
							sw=215
						elif dil1[0]['word'] == en_pronouns[1]: 
							sw=216
						elif dil1[0]['word'] == en_pronouns[5]: 
							sw=217
						elif dil1[0]['word'] == en_pronouns[7]: 
							sw=218
					
					elif len(dil4) == 1:					
						if dil4[0]['word'] == en_pronouns[0]: 
							sw=219
						elif dil4[0]['word'] == en_pronouns[1]: 
							sw=220
						elif dil4[0]['word'] == en_pronouns[5]: 
							sw=221
						elif dil4[0]['word'] == en_pronouns[7]: 
							sw=222
						
					elif len(dil6) == 1:
						if dil6[0]['word'] == en_pronouns[0]: 
							sw=223
						elif dil6[0]['word'] == en_pronouns[1]: 
							sw=224
						elif dil6[0]['word'] == en_pronouns[5]: 
							sw=225
						elif dil6[0]['word'] == en_pronouns[7]: 
							sw=226
				
				elif p3 == 'VBP' and p1 == 'VBG': 
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]: 
							sw=227
						elif dil1[0]['word'] == en_pronouns[1]: 
							sw=228
						elif dil1[0]['word'] == en_pronouns[5]: 
							sw=229
						elif dil1[0]['word'] == en_pronouns[7]: 
							sw=230
					
					elif len(dil4) == 1:	
						if dil4[0]['word'] == en_pronouns[0]: 
							sw=231
						elif dil4[0]['word'] == en_pronouns[1]: 
							sw=232
						elif dil4[0]['word'] == en_pronouns[5]: 
							sw=233
						elif dil4[0]['word'] == en_pronouns[7]: 
							sw=234
					
					elif len(dil6) == 1:
						if dil6[0]['word'] == en_pronouns[0]: 
							sw=235
						elif dil6[0]['word'] == en_pronouns[1]: 
							sw=236
						elif dil6[0]['word'] == en_pronouns[5]: 
							sw=237
						elif dil6[0]['word'] == en_pronouns[7]: 
							sw=238
						
				elif p3 == 'VBD' and p1 == 'VBG': 
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]:
							sw=239
						elif dil1[0]['word'] == en_pronouns[1]:
							sw=240
						elif dil1[0]['word'] in en_pronouns[2:5]:
							sw=241
						elif dil1[0]['word'] == en_pronouns[5]:
							sw=242
						elif dil1[0]['word'] == en_pronouns[7]:
							sw=243
					
					elif len(dil4) == 1:
						if dil4[0]['word'] == en_pronouns[0]:
							sw=244
						elif dil4[0]['word'] == en_pronouns[1]:
							sw=245
						elif dil4[0]['word'] in en_pronouns[2:5]:
							sw=246
						elif dil4[0]['word'] == en_pronouns[5]:
							sw=247
						elif dil4[0]['word'] == en_pronouns[7]:
							sw=248
						
					elif len(dil6) == 1:
						if dil6[0]['word'] == en_pronouns[0]:
							sw=249
						elif dil6[0]['word'] == en_pronouns[1]:
							sw=250
						elif dil6[0]['word'] in en_pronouns[2:5]:
							sw=251
						elif dil6[0]['word'] == en_pronouns[5]:
							sw=252
						elif dil6[0]['word'] == en_pronouns[7]:
							sw=253
			elif len(dil2) == 1 and len(dil3) == 1:
			
				if p3 == 'MD' and p9 == 'VB' and p1 == 'VBN':  
					if len(dil4) == 1:
						if dil4[0]['word'] == en_pronouns[0]:
							sw=254
						elif dil4[0]['word'] == en_pronouns[1]:
							sw=255
						elif dil4[0]['word'] in en_pronouns[2:5]:
							sw=256
						elif dil4[0]['word'] == en_pronouns[5]:
							sw=257
						elif dil4[0]['word'] == en_pronouns[7]:
							sw=258
							
				elif p3 == 'VBD' and p9 == 'VBN' and p1 == 'VBN':  
					if len(dil4) == 1:
						if dil4[0]['word'] == en_pronouns[0]:
							sw=259
						elif dil4[0]['word'] == en_pronouns[1]:
							sw=260
						elif dil4[0]['word'] in en_pronouns[2:5]:
							sw=261
						elif dil4[0]['word'] == en_pronouns[5]:
							sw=262
						elif dil4[0]['word'] == en_pronouns[7]:
							sw=263
							
				elif p3 == 'VBP' and p9 == 'VBN' and p1 == 'VBN':  
					if len(dil4) == 1:
						if dil4[0]['word'] == en_pronouns[0]:
							sw=264
						elif dil4[0]['word'] == en_pronouns[1]:
							sw=265
						elif dil4[0]['word'] == en_pronouns[5]:
							sw=266
						elif dil4[0]['word'] == en_pronouns[7]:
							sw=267
							
				elif p3 == 'VBZ' and p9 == 'VBN' and p1 == 'VBN':   
					if len(dil4) == 1:
						if dil4[0]['word'] in en_pronouns[2:5]:
							sw=268
			
			elif len(dil2) == 2 and len(dil3) == 0:
				if p4 == 'VBD' and p5 == 'VBN' and p1 == 'VBG': 
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]:
							sw=318
						elif dil1[0]['word'] == en_pronouns[1]:
							sw=319
						elif dil1[0]['word'] in en_pronouns[2:5]:
							sw=320
						elif dil1[0]['word'] == en_pronouns[5]:
							sw=321
						elif dil1[0]['word'] == en_pronouns[7]:
							sw=322
				elif p4 == 'VBZ' and p5 == 'VBN' and p1 == 'VBG': 
					sw=301
				elif p4 == 'MD' and p5 == 'VB' and p1 == 'VBG': 
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]:
							sw=302
						elif dil1[0]['word'] == en_pronouns[1]:
							sw=303
						elif dil1[0]['word'] in en_pronouns[2:5]:
							sw=304
						elif dil1[0]['word'] == en_pronouns[5]:
							sw=305
						elif dil1[0]['word'] == en_pronouns[7]:
							sw=306
					
					elif len(dil4) == 1:
						if dil4[0]['word'] == en_pronouns[0]:
							sw=307
						elif dil4[0]['word'] == en_pronouns[1]:
							sw=308
						elif dil4[0]['word'] in en_pronouns[2:5]:
							sw=309
						elif dil4[0]['word'] == en_pronouns[5]:
							sw=310
						elif dil4[0]['word'] == en_pronouns[7]:
							sw=311
						
					elif len(dil6) == 1:
						if dil6[0]['word'] == en_pronouns[0]:
							sw=312
						elif dil6[0]['word'] == en_pronouns[1]:
							sw=313
						elif dil6[0]['word'] in en_pronouns[2:5]:
							sw=314
						elif dil6[0]['word'] == en_pronouns[5]:
							sw=315
						elif dil6[0]['word'] == en_pronouns[7]:
							sw=316
						
						
				elif p4 == 'VBP' and p5 == 'VBN' and p1 == 'VBG': 
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]:
							sw=323
						elif dil1[0]['word'] == en_pronouns[1]:
							sw=324
						elif dil1[0]['word'] == en_pronouns[5]:
							sw=325
						elif dil1[0]['word'] == en_pronouns[7]:
							sw=326
			
			elif (len(dil2) == 3 and len(dil3) == 0) or (len(dil2) == 2 and len(dil3) == 1): 
				if p6 == 'MD' and p7 == 'VBD' and p8 == 'VBN' and p1 == 'VBG': 
					sw=400
				elif p6 == 'MD' and p7 == 'VB' and p8 == 'VBN' and p1 == 'VBG': 
					sw=401
				elif p6 == 'MD' and p7 == 'VBD' and p8 == 'VBN' and p1 == 'VBN': 
					if len(dil4) == 1:	
						if dil4[0]['word'] == en_pronouns[0]: 
							sw=418
						elif dil4[0]['word'] == en_pronouns[1]: 
							sw=419
						elif dil4[0]['word'] in en_pronouns[2:5]: 
							sw=420
						elif dil4[0]['word'] == en_pronouns[5]:
							sw=421
						elif dil4[0]['word'] == en_pronouns[7]:
							sw=422
							
				elif p6 == 'MD' and p7 == 'VB' and p8 == 'VBN' and p1 == 'VBN':
					if len(dil1) == 1:
						if dil1[0]['word'] == en_pronouns[0]: 
							sw=403
						elif dil1[0]['word'] == en_pronouns[1]: 
							sw=404
						elif dil1[0]['word'] in en_pronouns[2:5]: 
							sw=405
						elif dil1[0]['word'] == en_pronouns[5]: 
							sw=406
						elif dil1[0]['word'] == en_pronouns[7]: 
							sw=407
						
					elif len(dil4) == 1:	
						if dil4[0]['word'] == en_pronouns[0]:
							sw=408
						elif dil4[0]['word'] == en_pronouns[1]:
							sw=409
						elif dil4[0]['word'] in en_pronouns[2:5]:
							sw=410
						elif dil4[0]['word'] == en_pronouns[5]:
							sw=411
						elif dil4[0]['word'] == en_pronouns[7]:
							sw=412
					
					elif len(dil6) == 1:
						if dil6[0]['word'] == en_pronouns[0]: 
							sw=413
						elif dil6[0]['word'] == en_pronouns[1]: 
							sw=414
						elif dil6[0]['word'] in en_pronouns[2:5]: 
							sw=415
						elif dil6[0]['word'] == en_pronouns[5]: 
							sw=416
						elif dil6[0]['word'] == en_pronouns[7]: 
							sw=417
				
		else:
			if len(dil2) == 0 and len(dil3) == 0:
				if p1 == 'VBD' and p2 in ['NNP','NN']:
					sw=500
				elif p1 == 'VBD' and p2 == 'JJ':
					sw=501
				elif p1 == 'VBD' and p2 in ['NNPS','NNS']:
					sw=502
				elif p1 == 'VBZ' and p2 in ['NNP','NN']:
					sw=503
				elif p1 == 'VBZ' and p2 == 'JJ':
					sw=504
				elif p1 == 'VBP' and p2 in ['NNPS','NNS']:
					sw=505
				elif p1 == 'VB' and p2 in ['NNPS','NNS']: 
					sw=506
				elif p1 == 'VB' and p2 in ['NNP','NN']: 
					sw=507
			elif len(dil2) == 0 and len(dil3) == 1:
			
				if p9 == 'VBP' and p1 == 'VBN' and p2 in ['NNPS','NNS']:
					sw=508
				elif p9 == 'VBZ' and p1 == 'VBN' and p2 in ['NNP','NN']:
					sw=509
				elif p9 == 'VBD' and p1 == 'VBN' and p2 in ['NNPS','NNS']: 
					sw=510
				elif p9 == 'VBD' and p1 == 'VBN' and p2 in ['NNP','NN']:
					sw=511
					
			elif len(dil2) == 1 and len(dil3) == 0:
				if p3 == 'VBD' and p1 == 'VBN' and p2 in ['NNP','NN']: 
					sw=600
				elif p3 == 'VBZ' and p1 == 'VBN' and p2 in ['NNP','NN']: 
					sw=601
				elif p3 == 'VBZ' and p1 == 'VBG' and p2 in ['NNP','NN']: 
					sw=602
				elif p3 == 'VBD' and p1 == 'VBG' and p2 in ['NNP','NN']: 
					sw=603
				elif p3 == 'MD' and p1 == 'VB' and p2 in ['NNP','NN']: 
					sw=604
				elif p3 == 'VBD' and p1 == 'VBN' and p2 in ['NNPS','NNS']: 
					sw=605
				elif p3 == 'VBP' and p1 == 'VBN' and p2 in ['NNPS','NNS']: 
					sw=606
				elif p3 == 'VBP' and p1 == 'VBG' and p2 in ['NNPS','NNS']: 
					sw=607
				elif p3 == 'VBD' and p1 == 'VBG' and p2 in ['NNPS','NNS']: 
					sw=608
				elif p3 == 'MD' and p1 == 'VB' and p2 in ['NNPS','NNS']: 
					sw=609
			
			elif len(dil2) == 1 and len(dil3) == 1:
			
				if p3 == 'MD' and p9 == 'VB' and p1 == 'VBN' and p2 in ['NNPS','NNS']: 
					sw=650
				elif p3 == 'MD' and p9 == 'VB' and p1 == 'VBN' and p2 in ['NNP','NN']:
					sw=651
				elif p3 == 'VBP' and p9 == 'VBN' and p1 == 'VBN' and p2 in ['NNPS','NNS']: 
					sw=652
				elif p3 == 'VBZ' and p9 == 'VBN' and p1 == 'VBN' and p2 in ['NNP','NN']:
					sw=653
				elif p3 == 'VBD' and p9 == 'VBN' and p1 == 'VBN' and p2 in ['NNPS','NNS']: 
					sw=654
				elif p3 == 'VBD' and p9 == 'VBN' and p1 == 'VBN' and p2 in ['NNP','NN']:
					sw=655
			
			elif len(dil2) == 2 and len(dil3) == 0:
				if p4 == 'VBD' and p5 == 'VBN' and p1 == 'VBG' and p2 in ['NNP','NN']: 
					sw=700	
				elif p4 == 'VBD' and p5 == 'VBN' and p1 == 'VBG' and p2 in ['NNPS','NNS']: 
					sw=701
				elif p4 == 'VBZ' and p5 == 'VBN' and p1 == 'VBG' and p2 in ['NNP','NN']: 
					sw=702
				elif p4 == 'VBP' and p5 == 'VBN' and p1 == 'VBG' and p2 in ['NNPS','NNS']: 
					sw=703
				elif p4 == 'MD' and p5 == 'VB' and p1 == 'VBG' and p2 in ['NNP','NN']: 
					sw=704		
				elif p4 == 'MD' and p5 == 'VB' and p1 == 'VBG' and p2 in ['NNPS','NNS']: 
					sw=705
					
			elif (len(dil2) == 3 and len(dil3) == 0) or (len(dil2) == 2 and len(dil3) == 1): 
				if p6 == 'MD' and p7 == 'VBD' and p8 == 'VBN' and p1 == 'VBG' and p2 in ['NNP','NN']: 
					sw=800
				elif p6 == 'MD' and p7 == 'VB' and p8 == 'VBN' and p1 == 'VBG' and p2 in ['NNP','NN']:
					sw=801
				elif p6 == 'MD' and p7 == 'VBD' and p8 == 'VBN' and p1 == 'VBN' and p2 in ['NNP','NN']:
					sw=802
				elif p6 == 'MD' and p7 == 'VB' and p8 == 'VBN' and p1 == 'VBN' and p2 in ['NNP','NN']: 
					sw=803
				if p6 == 'MD' and p7 == 'VBD' and p8 == 'VBN' and p1 == 'VBG' and p2 in ['NNPS','NNS']: 
					sw=804
				elif p6 == 'MD' and p7 == 'VB' and p8 == 'VBN' and p1 == 'VBG' and p2 in ['NNPS','NNS']:
					sw=805
				elif p6 == 'MD' and p7 == 'VBD' and p8 == 'VBN' and p1 == 'VBN' and p2 in ['NNPS','NNS']: 
					sw=806
				elif p6 == 'MD' and p7 == 'VB' and p8 == 'VBN' and p1 == 'VBN' and p2 in ['NNPS','NNS']:
					sw=807
	

	return sw
def find_dependent(dep_list,dep,verb,index):
	dep_idx=[]
	for e in dep_list:
		
		if e['dep'] == dep:
			if e['governorGloss'] == verb and e['governor'] == index:
				d={'word':e['dependentGloss'],'idx':e['dependent']}
				dep_idx.append(d)
			elif e['dependentGloss'] == verb and e['dependent'] == index:
				d={'word':e['governorGloss'],'idx':e['governor']}
				dep_idx.append(d)
	
	return dep_idx

def find_pos(pos_list,d):		
	pos=''
	for e in pos_list:
		if e['index'] == d['idx'] and e['word'] == d['word']: 
			pos=e['pos']
			break
	return pos

