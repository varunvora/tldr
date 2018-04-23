from math import log
from pickle import load
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
from random import randrange
from word_score import get_word_score
from dataset_loader import load_dataset

def sentence_score(sentence, word_score_dictionary, log_probability = False) :
	context_words = [word for word in word_tokenize(sentence) if word not in stopwords and len(word)>1]
	if not log_probability :
		return sum([word_score_dictionary[word] for word in context_words])/(len(context_words) + 0.01)
	else :
		score = 0
		total_context_words = len(context_words)
		for word in context_words :
			if word_score_dictionary[word] != 0 :
				score += log(word_score_dictionary[word],2)
			else :
				total_context_words -= 1
		total_context_words += 0.01		
		return score / total_context_words

def extractive_summarizer(article, word_score_dictionary, sentence_count = 10, log_probability = False) :
	sentences = sent_tokenize(article)
	sentences.sort(key = lambda x : sentence_score(x, word_score_dictionary, log_probability = log_probability), reverse = True)
	chosen_sentences = set(sentences[:sentence_count])
	summary = [sentence for sentence in sent_tokenize(article) if sentence in chosen_sentences]
	return " ".join(summary)

if __name__ == "__main__" :
	with open('clean_dataset.pkl', 'rb') as fp:
		article_word_list, summary_word_list = load(fp)

	word_score_dictionary = get_word_score(article_word_list, summary_word_list)
	print("NORMAL PROBABILITY")
	#article = "ON WEDNESDAY, AT about 12:15 pm EST, 1.35 terabits per second of traffic hit the developer platform GitHub all at once. It was the most powerful distributed denial of service attack recorded to date—and it used an increasingly popular DDoS method, no botnet required. GitHub briefly struggled with intermittent outages as a digital system assessed the situation. Within 10 minutes it had automatically called for help from its DDoS mitigation service, Akamai Prolexic. Prolexic took over as an intermediary, routing all the traffic coming into and out of GitHub, and sent the data through its scrubbing centers to weed out and block malicious packets. After eight minutes, attackers relented and the assault dropped off. The scale of the attack has few parallels, but a massive DDoS that struck the internet infrastructure company Dyn in late 2016 comes close. That barrage peaked at 1.2 terabits per second and caused connectivity issues across the US as Dyn fought to get the situation under control. “We modeled our capacity based on fives times the biggest attack that the internet has ever seen,” Josh Shaul, vice president of web security at Akamai told WIRED hours after the GitHub attack ended. “So I would have been certain that we could handle 1.3 Tbps, but at the same time we never had a terabit and a half come in all at once. It’s one thing to have the confidence. It’s another thing to see it actually play out how you’d hope."
	x, y = load_dataset()
	
	seed = 2
	article = x[seed]
	actual_summary = y[seed]
	summary = extractive_summarizer(article, word_score_dictionary, sentence_count = 6)

	print("ARTICLE", article, sep = "\n")
	print("SUMMARY", summary, sep = "\n")
	print("ACTUALLY ", actual_summary,  sep = "\n")

	print("Approximate words in the article", len(article.split()))
	print("Approximate words in the summary", len(summary.split()))

	quit()
	print("LOG PROBABILITY")
	summary = extractive_summarizer(article, word_score_dictionary, sentence_count = 4, log_probability = True)	
	
	print("ARTICLE", article, sep = "\n")
	print("SUMMARY", summary, sep = "\n")

	print("Approximate words in the article", len(article.split()))
	print("Approximate words in the summary", len(summary.split()))