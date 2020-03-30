def convert_penn_treebank_tagset(ugposl):
	ptbts=['CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NNS','NNP','NNPS','PDT','POS','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB']
	posl=['n.','v.','adj.','adv.','prep.','conj.','interj.','vtr.','vtran.','vintr.','vintran.','intr.','excl.','pron.','num.','comp.','int.','superl.','asj.','prefix.','abbr.','article.','tr.']
	
	list=[]
	for d in ugposl:
		if d['pos'] == ptbts[0]:
			dict={'word': d['word'], 'pos': posl[5], 'alt_pos': posl[5], 'penn_pos': ptbts[0]}
			list.append(dict)
		elif d['pos'] == ptbts[1]:
			dict={'word': d['word'], 'pos': posl[14], 'alt_pos': posl[14], 'penn_pos': ptbts[1]}
			list.append(dict)
		elif d['pos'] == ptbts[2]:
			dict={'word': d['word'], 'pos': posl[21], 'alt_pos': posl[21], 'penn_pos': ptbts[2]}
			list.append(dict)
		elif d['pos'] == ptbts[3]:
			dict={'word': d['word'], 'pos': posl[3], 'alt_pos': posl[3], 'penn_pos': ptbts[3]}
			list.append(dict)
		elif d['pos'] == ptbts[4]:
			dict={'word': d['word'], 'pos': '', 'alt_pos': '', 'penn_pos': ptbts[4]}
			list.append(dict)
		elif d['pos'] == ptbts[5]:
			dict={'word': d['word'], 'pos': posl[4], 'alt_pos': posl[4], 'penn_pos': ptbts[5]}
			list.append(dict)
		elif d['pos'] == ptbts[6]:
			dict={'word': d['word'], 'pos': posl[2], 'alt_pos': posl[18], 'penn_pos': ptbts[6]}
			list.append(dict)
		elif d['pos'] == ptbts[7]:
			dict={'word': d['word'], 'pos': posl[15], 'alt_pos': posl[2], 'penn_pos': ptbts[7]}
			list.append(dict)
		elif d['pos'] == ptbts[8]:
			dict={'word': d['word'], 'pos': posl[17], 'alt_pos': posl[2], 'penn_pos': ptbts[8]}
			list.append(dict)
		elif d['pos'] == ptbts[9]:
			dict={'word': d['word'], 'pos': '', 'alt_pos': '', 'penn_pos': ptbts[9]}
			list.append(dict)
		elif d['pos'] == ptbts[10]:
			dict={'word': d['word'], 'pos': posl[1], 'alt_pos': posl[1], 'penn_pos': ptbts[10]}
			list.append(dict)
		elif d['pos'] == ptbts[11]:
			dict={'word': d['word'], 'pos': posl[0], 'alt_pos': posl[0], 'penn_pos': ptbts[11]}
			list.append(dict)
		elif d['pos'] == ptbts[12]:
			dict={'word': d['word'], 'pos': posl[0], 'alt_pos': posl[0], 'penn_pos': ptbts[12]}
			list.append(dict)
		elif d['pos'] == ptbts[13]:
			dict={'word': d['word'], 'pos': posl[0], 'alt_pos': posl[0], 'penn_pos': ptbts[13]}
			list.append(dict)
		elif d['pos'] == ptbts[14]:
			dict={'word': d['word'], 'pos': posl[0], 'alt_pos': posl[0], 'penn_pos': ptbts[14]}
			list.append(dict)
		elif d['pos'] == ptbts[15]:
			dict={'word': d['word'], 'pos': posl[2], 'alt_pos': posl[2], 'penn_pos': ptbts[15]}
			list.append(dict)
		elif d['pos'] == ptbts[16]:
			dict={'word': d['word'], 'pos': '', 'alt_pos': '', 'penn_pos': ptbts[16]}
			list.append(dict)
		elif d['pos'] == ptbts[17]:
			dict={'word': d['word'], 'pos': posl[13], 'alt_pos': posl[13], 'penn_pos': ptbts[17]}
			list.append(dict)
		elif d['pos'] == ptbts[18]:
			dict={'word': d['word'], 'pos': posl[13], 'alt_pos': posl[13], 'penn_pos': ptbts[18]}
			list.append(dict)
		elif d['pos'] == ptbts[19]:
			dict={'word': d['word'], 'pos': posl[3], 'alt_pos': posl[3], 'penn_pos': ptbts[19]}
			list.append(dict)
		elif d['pos'] == ptbts[20]:
			dict={'word': d['word'], 'pos': posl[3], 'alt_pos': posl[3], 'penn_pos': ptbts[20]}
			list.append(dict)
		elif d['pos'] == ptbts[21]:
			dict={'word': d['word'], 'pos': posl[3], 'alt_pos': posl[3], 'penn_pos': ptbts[21]}
			list.append(dict)
		elif d['pos'] == ptbts[22]:
			dict={'word': d['word'], 'pos': posl[3], 'alt_pos': posl[3], 'penn_pos': ptbts[22]}
			list.append(dict)
		elif d['pos'] == ptbts[23]:
			dict={'word': d['word'], 'pos': '', 'alt_pos': '', 'penn_pos': ptbts[23]}
			list.append(dict)
		elif d['pos'] == ptbts[24]:
			dict={'word': d['word'], 'pos': posl[4], 'alt_pos': posl[4], 'penn_pos': ptbts[24]}
			list.append(dict)
		elif d['pos'] == ptbts[25]:
			dict={'word': d['word'], 'pos': posl[6], 'alt_pos': posl[16], 'penn_pos': ptbts[25]}
			list.append(dict)
		elif d['pos'] == ptbts[26]:
			dict={'word': d['word'], 'pos': posl[1], 'alt_pos': ptbts[26], 'penn_pos': ptbts[26]}
			list.append(dict)
		elif d['pos'] == ptbts[27]:
			dict={'word': d['word'], 'pos': posl[1], 'alt_pos': ptbts[27], 'penn_pos': ptbts[27]}
			list.append(dict)
		elif d['pos'] == ptbts[28]:
			dict={'word': d['word'], 'pos': posl[1], 'alt_pos': ptbts[28], 'penn_pos': ptbts[28]}
			list.append(dict)
		elif d['pos'] == ptbts[29]:
			dict={'word': d['word'], 'pos': posl[1], 'alt_pos': ptbts[29], 'penn_pos': ptbts[29]}
			list.append(dict)
		elif d['pos'] == ptbts[30]:
			dict={'word': d['word'], 'pos': posl[1], 'alt_pos': ptbts[30], 'penn_pos': ptbts[30]}
			list.append(dict)
		elif d['pos'] == ptbts[31]:
			dict={'word': d['word'], 'pos': posl[1], 'alt_pos': ptbts[31], 'penn_pos': ptbts[31]}
			list.append(dict)
		elif d['pos'] == ptbts[32]:
			dict={'word': d['word'], 'pos': posl[13], 'alt_pos': posl[5], 'penn_pos': ptbts[32]}
			list.append(dict)
		elif d['pos'] == ptbts[33]:
			dict={'word': d['word'], 'pos': posl[13], 'alt_pos': posl[2], 'penn_pos': ptbts[33]}
			list.append(dict)
		elif d['pos'] == ptbts[34]:
			dict={'word': d['word'], 'pos': posl[13], 'alt_pos': posl[13], 'penn_pos': ptbts[34]}
			list.append(dict)
		elif d['pos'] == ptbts[35]:
			dict={'word': d['word'], 'pos': posl[3], 'alt_pos': posl[5], 'penn_pos': ptbts[35]}
			list.append(dict)
			
		else:
			dict={'word': d['word'], 'pos': d['pos'], 'alt_pos': d['pos'], 'penn_pos': d['pos']}
			list.append(dict)
	

	return list
			