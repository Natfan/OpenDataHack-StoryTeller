import nltk;

dt = [];
vb = [];
nn = [];
wdt = [];
rb = [];
jj = [];
conj = [];
gmr = [];
ignore = [];

verbose = True;

def getWordTypes(text):
	text = nltk.word_tokenize(text);
	words = nltk.pos_tag(text);
	if verbose == True:
		for item, index in words:
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
	else:
		print words;

#TODO:
#	1. get frank.txt
#	2. get rndm pos in frank
#	3. select 140 chars max with  

getWordTypes("why hello my fellow human. i am not a robot, i am alive! a real boy, i do declare my variables");
