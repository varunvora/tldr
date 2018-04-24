from math import log
from pickle import load, dump
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
from random import randrange
from word_score import get_word_score
from dataset_loader import load_dataset
from sentence_score import extractive_summarizer 
import string 





if __name__ == "__main__" :
	with open('dataset.pkl', 'rb') as fp:
		article_word_list, summary_word_list = load(fp)

	word_score_dictionary = get_word_score(article_word_list, summary_word_list)
	x, y = load_dataset()
	fixed_x = []
	for i in range(len(x)):
		x[i].maketrans('','', string.punctuation)
		if(len(x[i].split()) > 150):
			ans = " ".join(e for e in x[i].split()[:100])
			fixed_x.append(ans)
		else:
			try :
				summary = extractive_summarizer(x[i], word_score_dictionary, sentence_count = 6)
			except ZeroDivisionError :
				continue

			z = summary.split()
			if(len(z)>100):
				ans = " ".join(e for e in z[:100])
				fixed_x.append(ans)
			else:
				pre_len = len(z)
				for i in range(100 - pre_len):
					z.append(z[randrange(pre_len)])
				ans = " ".join(e for e in z)	
				fixed_x.append(ans)
	
	a=[]			
	for i in fixed_x:
		a.append(len(i.split()))			
	print(set(a))
	with open('fixed_len_dataset.pkl','wb') as fp :
		dump((fixed_x),fp)