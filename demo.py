from sentence_score import extractive_summarizer
from abstractive import abstractive_summarizer
from word_score import get_word_score
from pickle import load
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from dataset_loader import load_dataset
import sys
import random
from os import system
porter = PorterStemmer()

def load_keras_model() :
	model = open("abstractive_model.h5")
	weights = model.weights
	return weights

if __name__ == "__main__" :
	x, y = load_dataset()
	seed = random.randrange(len(x))
	with open('dataset.pkl', 'rb') as fp:
		article_word_list, summary_word_list = load(fp)

	word_score_dictionary = get_word_score(article_word_list, summary_word_list)
	system('figlet TLDR ')
	choice = input("Choose one of the following\n1. New article\n2. Random article from dataset\nYour choice : ")
	if choice == "1" :
		f = open("article_file.txt", "r")
		article = f.read()
		f.close()
		article = " ".join(article.split())
	elif choice == "2" :
		article = x[seed]
		actual_summary = y[seed]
	else :
		print("Invalid choice")
		quit()
	space = "---"*72 + "--"
	ex_summary = extractive_summarizer(article, word_score_dictionary, sentence_count = 3)
	ab_summary = abstractive_summarizer(article, word_score_dictionary, sentence_count = 3)
	ab_summary = ' '.join(ab_summary.split()[:60])
	
	print(space)	
	print("ARTICLE", article, sep = "\n")
	print()
	print(space)
	if choice == "2" :
		print("ACTUAL SUMMARY\n", actual_summary,  sep = "\n")
		print(space)
	print("EXTRACTIVE SUMMARY\n", ex_summary, sep = "\n")
	print(space)
	print("ABSTRACTIVE SUMMARY\n", ab_summary, sep = "\n")
	print(space)
	

	
