# TODO:
#  DATA:
#   1. get data from site
#   2. analyse data that we have got
#
#  PROG:
#   1. make 4 arrays with 3spaces for bool values (3d array??)
#   2.
import nltk;

print("version 2");

#text = 'This is a sentence that contains some words. These words are sometimes long, but mostly short. I like words, some may even say that I have the best words!';
text = 'could i possibly have eaten your cheese?'
text = nltk.word_tokenize(text);
result = nltk.pos_tag(text);

dt = [];
vb = [];
nn = [];
wdt = [];
rb = [];
jj = [];
conj = [];
gmr = [];
ignore = [];

#result = [i for i in result if i[0].lower == 'words']

for item, index in result:
	if index == 'DT' or index == 'PRP$':
		dt.append(item);
	if index == 'VB' or index == 'VBD' or index == 'VBG' or index == 'VBN' or index == 'VBP' or index == 'VBZ':
		vb.append(item);
	if index == 'NN' or index == 'NNS' or index == 'NNP' or index == 'NNPS' or index == 'PRP':
		nn.append(item);
	if index == 'WDT':
		wdt.append(item);
	if index == 'RB' or index == 'RBR' or index == 'RBS':
		rb.append(item);
	if index == 'CC' or index == 'IN':
		conj.append(item);
	if index == 'JJ' or index == 'JJR' or index == 'JJS':
		jj.append(item);
	if index == 'IN':
		conj.append(item);
	if index == '?' or index == 'WRB' or ignore == 'MD':
		ignore.append(item);
	if index == ',' or index == '.' or index == '!':
		gmr.append(item);
print("");
print "Determiner", dt;
print("");
print "Verb", vb;
print("");
print "Noun", nn;
print("");
print "WH-Determiner", wdt;
print("");
print "Adverb", rb;
print("");
print "Adjective", jj;
print("");
print "Conjuction", conj;
print("");
print "Grammar", gmr;
print("");
print "Ignore", ignore;
print("");

print result;
