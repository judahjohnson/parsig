def consecutive_blocks(idx_list):
	blocks_mtrx=[]
	from itertools import groupby
	from operator import itemgetter
	for k, g in groupby(enumerate(idx_list), lambda (i, x): i-x):
		
		blocks_mtrx.append(map(itemgetter(1), g))
	return blocks_mtrx