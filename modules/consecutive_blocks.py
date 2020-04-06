def consecutive_blocks(idx_list):	
	
	import more_itertools
	return [list(group) for group in more_itertools.consecutive_groups(idx_list)]