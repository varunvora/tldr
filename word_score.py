# Sw word is in summary.
# Wi occurence of a particular word.
# P(x) is probability of x

from collections import Counter
from pickle import load

def get_word_score(article_word_list, summary_word_list) :
	Na = len(article_word_list) # total number of words in the articles
	Ns = len(summary_word_list) # total number of words in the summaries

	article_word_dict = Counter(article_word_list)
	summary_word_dict = Counter(summary_word_list)
	combined_dict = article_word_dict + summary_word_dict

	Va = len(article_word_dict) # number of unique words in the articles
	Vs = len(summary_word_dict) # number of unique words in the summaries

	# P(Wi | Sw)
	P_Wi_given_Sw = Counter({word : summary_word_dict[word] / Ns for word in summary_word_dict})

	# P(Sw)
	P_Sw = Ns / (Na + Ns)

	# P(Wi)
	P_Wi = Counter({word : (combined_dict[word]) / (Na + Ns) for word in combined_dict})

	# P(Sw | Wi)
	word_score = Counter({word : P_Wi_given_Sw[word] * P_Sw / P_Wi[word] for word in article_word_dict})

	print("Va: ", Va)
	print("Vs: ", Vs)
	print("Na: ", Na)
	print("Ns: ", Ns)

	return word_score

if __name__ == "__main__" :
	with open('clean_dataset.pkl', 'rb') as fp:
		article_word_list, summary_word_list = load(fp)

	word_score = get_word_score(article_word_list, summary_word_list)
	print(word_score.most_common(10))


 