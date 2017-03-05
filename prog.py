import nltk;
from random import randint;

dt = [];
vb = [];
nn = [];
wdt = [];
rb = [];
jj = [];
conj = [];
gmr = [];
ignore = [];

wordlist = [];
textline = [];

frankfilenotSQL = 'words/frank.csv';

verbose = 0;

def getWordTypes(text):
	if not text:
		wordlist.append("ERROR");
	text = nltk.word_tokenize(text);
	words = nltk.pos_tag(text);
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
	if verbose == 1:
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

def getTypes(text, lookingfor1, lookingfor2, lookingfor3):
	lf1b = 0
	lf2b = 0
	lf3b = 0

	wordTypes = getWordTypes(text);

	if (lookingfor1 == 'dt'):
		lf1b = dt;
	if (lookingfor1 == 'vb'):
		lf1b = vb;
	if (lookingfor1 == 'nn'):
		lf1b = nn;
	if (lookingfor1 == 'wdt'):
		lf1b = wdt;
	if (lookingfor1 == 'rb'):
		lf1b = rb;
	if (lookingfor1 == 'jj'):
		lf1b = jj;
	if (lookingfor1 == 'conj'):
		lf1b = conj;
	if (lookingfor1 == 'gmr'):
		lf1b = gmr;

	if (lookingfor2 == 'dt'):
		lf2b = dt;
	if (lookingfor2 == 'vb'):
		lf2b = vb;
	if (lookingfor2 == 'nn'):
		lf2b = nn;
	if (lookingfor2 == 'wdt'):
		lf2b = wdt;
	if (lookingfor2 == 'rb'):
		lf2b = rb;
	if (lookingfor2 == 'jj'):
		lf2b = jj;
	if (lookingfor2 == 'conj'):
		lf2b = conj;
	if (lookingfor2 == 'gmr'):
		lf2b = gmr;

	if (lookingfor3 == 'dt'):
		lf3b = dt;
	if (lookingfor3 == 'vb'):
		lf3b = vb;
	if (lookingfor3 == 'nn'):
		lf3b = nn;
	if (lookingfor3 == 'wdt'):
		lf3b = wdt;
	if (lookingfor3 == 'rb'):
		lf3b = rb;
	if (lookingfor3 == 'jj'):
		lf3b = jj;
	if (lookingfor3 == 'conj'):
		lf3b = conj;
	if (lookingfor3 == 'gmr'):
		lf3b = gmr;

	if (len(lf1b) == 0):
		print "FAIL, LF1B is NULL"
		return False
	if (len(lf2b) == 0):
		print "FAIL, LF2B is NULL"
		return False
	if len(lf3b) == 0:
		print "FAIL, LF3B is NULL"
		return False;

	output = [lf1b, lf2b, lf3b];
	return output;

def updateWordList():
	with open('words/nouns.csv', 'r') as myfile:
	    wordlist=myfile.read().split('\n');
	return wordlist

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getTextFile(filename, no1, no2, no3):
	print "start"
	randomNo = randint(0, (file_len(filename)-1));
	print randomNo
	repeat = True
	with open(filename, 'r') as frank:
		print "start openfile"
		frank.seek(randomNo);
		print "seeking"
		while repeat == True:
			print "reading line"
			frank.readline();
			print "assigning readline to local var"
			textline = frank.readline();
			print "starting if to check leng"
			if (len(textline) <= 10 or len(textline) >= 140):
				print "setting types to getTypes vals"
				types = getTypes(textline, no1, no2, no3)
				print "if types is false, restart while"
				if (types != False):
					print "success!"
					outputs = [textline, types];
					repeat = False;
			else:
				print "sentence is too short"
				repeat = True;
		return textline;

#TODO:
#	1. get frank.txt DONE
#	2. get rndm pos in frank DONE
#	3. select a sentence that is 140 chars max with  a lower limit of 10

wordlist = updateWordList();

textwords = ' '.join(wordlist);

#getWordTypes(textwords);

print("");

outputTextFile = getTextFile(frankfilenotSQL, 'nn', 'nn', 'jj');

#print outputTextFile;

print("");

print getTypes(outputTextFile, 'nn', 'wdt', 'rb');
# print getTypes(outputTextFile, 'vb');
# print getTypes(outputTextFile, 'nn');
# print getTypes(outputTextFile, 'wdt');
# print getTypes(outputTextFile, 'rb');
# print getTypes(outputTextFile, 'jj');
# print getTypes(outputTextFile, 'conj');
# print getTypes(outputTextFile, 'gmr');