1. Word sense disambiguation for English homonyms
It is easy to implement this feature for words which have multiple meanings, e.g., 2 senses for word "pound" are (a) unit of weight (b) to beat (check word_sense_disambiguation.py in parsig/modules/ folder). However, since we didn't create a dictionary of English homonyms which is machine readable, we didn't enable this feature. We need help with creating a dictionary of English homonyms in excel. Following is an example: 1st column: English word or phrase, 2nd column: 1st meaning, 3rd column: 1st sense, 4th column: 2nd meaning, 5th column: 2nd sense, etc. So, corresponding rows for word "pound" in the excel file is as follows (we just have 2 columns for the time being): 
1st column: pound, 2nd column: pound, 3rd column: weight, 4th column: kōb, 5th column: beat
1st column: pound, 2nd column: pound, 3rd column: weight, 4th column: kuftan, 5th column: beat

2. English phrasal verbs
This feature is also not implemented, as we didn't create a dictionary of English phrasal verbs. These verbs have multiple meanings occasionally, and we need help with creating a dictionary of English phrasal verbs in excel. 
Following is an example of the corresponding row for phrase "break off" (we just have 2 columns for the time being): 
1st column: break_off, 2nd column: ō ham madan, 3rd column: end, 4th column: appārēnīdan, 5th column: remove, 6th column: peyrāmīdan, 7th column: stop

3. Transitive vs intransitive verbs 
This feature is also not implemented, since we didn't create a corresponding column for verbs. 

4. Verb tenses
We have implemented following verb tenses (check verb_tense_and_inflection.py and dep_pos_based_suffix.py). Following examples are assumed to be past tense (we have to make sure if this assumption is correct):
I went -> šud ham, 
I was happy -> šād būd ham, 
I was defeated -> stōbēnīd ham, 
I was going -> šud ham, 
I had been going -> šud ham, 
I have been going -> šud ham.  
Following examples are assumed to be present tense (we have to make sure if this assumption is correct):
I go -> šavam, 
I am happy -> šād bavam, 
I am defeated -> stōb kunam, 
I am going -> šavam, 
I will be happy -> šād bavam, 
I will go -> šavam, 
I will be defeated -> stōb kunam, 
I will be going -> šavam.  
Following examples are assumed to be present perfect tense (we have to make sure if this assumption is correct):
I have gone -> šud estam, 
I have been defeated -> stōbēnīd estam.  
If there's a modal, e.g., "should" or "could", we'll apply the following rule:
I should have been gone -> šāyam šudan, 
I should have been defeated -> šāyam stōbēnīdan.  
Following examples are all assumed to be past perfect tense (we have to make sure if this assumption is correct):
I had gone -> šud būd ham, 
I had been defeated -> stōbēnīd būd ham, 
should had been gone -> šud būd ham, 
should had been defeated -> stōbēnīd būd ham.  
This feature is disabled for the time being, to improve the performance. We need to know if any of these rules are incorrect, or if we could improve them.

5. English vs Pārsīg order of words
English vs Pārsīg order of words in a given sentence are different, e.g.,  I{0} am_expecting{1} a{2} parcel{3} from{4} Pārs{5} -> an{0} bastag{3} -ē{2} az{4} pārs{5} pehikaham{1}. This feature was implemented in the beginning, using ibm2 statistical machine translation model (check main.py in parsig/ folder). However, ibm2 implementation is disabled for the time being, as it has the following cons: (a) it becomes very slow as size of training data set increases, which is a big issue. The purpose of this project was to automate uploading thousands of articles on Wikipedia, or hundreds of books, while not compromising the quality. However, as we didn't have committed personnel and enough computers to translate in parallel, we decided to disable this feature as it won't compromise quality that much. (b) SMT also removes some words in target (Pārsīg). This makes it even harder to edit the Pārsīg text, especially, if people who are editing are not that familiar with Pārsīg. However, as Farsi grammar and Pārsīg grammar are very similar, anyone who speaks Farsi and knows English, would be able to improve the Pārsīg word order, just by knowing the one-to-one mapping between source (English) and target (Pārsīg) words. To do this, we enumerate words on both sides inside curly brackets (source and target). (c) Even if we enable this feature, it is not 100% accurate (accuracy varies between 50%-80% approximately). So, to have a flawless translation, we still need humans, to edit the order of words. 

6. Jargon/terminology/index
This is also a big challenge, as a lot of technical words are missing on Pārsīg dictionary, e.g., "transistor". Since we didn't create a dictionary of technical terms, we decided to enable the user to add technical words on a separate excel file. Check path_list.xlsx in parsig/ folder. Column "a" represents text, and column "b" represents corresponding terms (or indices). We won't translate the words which are added onto the terms list. So, a given word which is a technical term for a text, will be an ordinary word for a different text, e.g., "current" is a technical word once text is about "electronics" (won't be translated into "pāyāg" even though it is in our Pārsīg dictionary), but it is an ordinary word once text is about "history" (will be translated into "pāyāg"). Another solution for this is to change the pronunciation and spelling, from source (English) to target (Pārsīg), based on some phonetic rules like ancient times, e.g., "Cyrus" for "Kūrauš". Please let us know if it is possible to create these phonetic rules, as it is very easy to create thousands of corresponding technical terms in Pārsīg using computers, this way.

7. English synonyms and English Pārsīg dictionary
We scraped the English Pārsīg dictionary on http://www.parsig.org/dictionary.html. The scraped dictionary has 3062 verbs, 10855 words (other than verbs), and 1368 phrases (check verbs.xlsx, unigrams.xlsx, and phrases.xlsx in parsig folder respectively). These many words are not suffice to translate every English article on Wikipedia, or every technical book into Pārsīg, since there are 470000 entries in Webster's 3rd New International Dictionary, Unabridged, together with its 1993 Addenda Section, as an example (check https://www.merriam-webster.com/help/faq-how-many-english-words). To fix this problem, we used the common 370103 English words at https://github.com/dwyl/english-words/blob/master/words_alpha.txt and created a 131754 to 13917 mapping, based on model at https://fasttext.cc/docs/en/english-vectors.html. 238349 words on words_alpha.txt were not on fasttext model. Check thesaurus.xlsx and generate_thesaurus.py in parsig/ folder. Models like fasttext are approximate, e.g., "Turkman" maps into "Zoroastrian", which is not accurate. We need help to improve this English-Pārsīg dictionary. We'll also need more columns for English homonyms, like the example shown in part 1.

8. To run the program, you need the following:
(a) Python 3 (program was first written in Python 2.7, however it was modified in Python 3.8.2 to fix some bugs). Check https://www.python.org/downloads/
(b) For dependency parsing, NER, and POS tagging, stanford-corenlp-full-2017-06-09 has been used. Unzip files in parsig/tanford-corenlp-full-2017-06-09/ folder. Check https://stanfordnlp.github.io/CoreNLP/history.html and https://stanfordnlp.github.io/CoreNLP/download.html. If a different version of Stanford CoreNLP is used, name of the folder has to be changed in main.py (check main.py in parsig/ folder)
(c) Following packages have been used (pip install <name> command can be used to install, e.g., pip install nltk): corenlp-pywrap, Cython, gensim, more-itertools, nltk, numpy, pandas, pdfminer, scipy, and xlrd.
(d) List each txt or pdf file path to be translated on parsig/path_list.xlsx column "a" and its corresponding terms path on column "b" on the same row, like the example which has been uploaded. Each file representing terms, is an xlsx file. This file has to have a single column "a", and corresponding terms have to be listed on this column.
