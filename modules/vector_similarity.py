def vector_similarity(vector1,vector2):
	import numpy as np
	if (np.linalg.norm(vector1)*np.linalg.norm(vector2)) !=0:
		cosine_angle=np.inner(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2))
	else:
		cosine_angle=0
		
	return cosine_angle