def scrub(word):
	import re
	word=re.sub(ur'( |-|\u002d|\u005f|\u00ad|\u0331|\u0332|\u0335|\u0336|\u2012|\u2013|\u2014|\u2015|\u2017|\u2212|\u2500)+', '_', word,re.UNICODE).strip()
	return re.sub(ur'(=|&|:|!|/|[.]|\u2019s|\u2019ll|\u2019m|\u2019ve|\u2019re|es\u2019|s\u2019|o\u2019|n\u2019t|;|[?]|,|-/|\(|\))+', '', word,re.UNICODE).lower().strip()
	