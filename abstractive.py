from sentence_score import extractive_summarizer
from word_score import get_word_score
from pickle import load
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import sys
import random
porter = PorterStemmer()

def normalize_text(text) :
    text = text.lower()
    text = text.replace("'", "") #wouldn't -> wouldnt
    for char in list(punctuation) : #remove all punctuation
        text = text.replace(char, " ")
    #text = " ".join(filter(lambda x : x not in stopwords , text.split())) #remove stopwords
    #text = " ".join(filter(lambda x : x.isalpha(), text.split())) #remove numbers
    text = " ".join([porter.stem(x) for x in text.split()]) #stemming
    text = " ".join(text.split()) #ensure words delimited by single space only
    return text

with open('clean_dataset.pkl', 'rb') as fp:
    article_word_list, summary_word_list = load(fp)

    word_score_dictionary = get_word_score(article_word_list, summary_word_list)

#article = "President Donald Trump twice gave James Comey an alibi for why a salacious report about the 2013 Miss Universe pageant in Moscow couldn’t be true: He never even spent the night in Russia during that trip, Trump told the former FBI director, according to Comey’s memos about the conversations.Yet the broad timeline of Trump’s stay, stretching from Friday, Nov. 8, 2013, through the following Sunday morning, has been widely reported. And it’s substantiated by social media posts that show he slept in Moscow the night before the Miss Universe contest.Now, flight records obtained by Bloomberg provide fresh details. Combined with existing accounts and Trump’s own social-media posts, they capture two days that, nearly five years later, loom large in the controversy engulfing the White House and at the heart of the Comey memos, which the Justice Department turned over last week to Congress.Neither the White House nor Trump Organization immediately responded to requests for comment.According to Comey’s accounts of his 2017 meetings with the president, Trump said the Moscow trip was so quick that his head never hit a pillow -- even for one night. Trump fired Comey on May 9, 2017."
#

def abstractive_summarizer(article, word_score_dictionary, sentence_count = 4, log_probability = True) :
	swap_erate=0.05
	swap_prob = 0.05
	remove_rate=0.1
	unk_rate=0.05
	lower_lim=0.1 ##starting percentage where errors should be introduced
	upper_lim=1 ##ending percentage after wich error should be avoided 
	summary = extractive_summarizer(article, word_score_dictionary, sentence_count = 4, log_probability = True)
	lsum=list(summary.split(" "));
#	print(lsum)
	for _ in range(3):
		swapping_indexes=random.sample(range(int(lower_lim*len(lsum)),int(upper_lim*len(lsum))),int(swap_erate*len(lsum)))
#		print('lowde')
	for i in swapping_indexes:
		if( i < len(lsum) - 1):
			temp=lsum[i]
			lsum[i]=lsum[i+1]
			lsum[i+1]=temp
	swapping_indexes=random.sample(range(int(lower_lim*len(lsum)),int(upper_lim*len(lsum))),int(remove_rate*len(lsum)))
	for i in swapping_indexes:
		lsum[i]=""
	lsum=normalize_text(" ".join(lsum))
	lsum = lsum.split()
	swapping_indexes=random.sample(range(int(lower_lim*len(lsum)),int(upper_lim*len(lsum))),int(remove_rate*len(lsum)))
	for i in swapping_indexes:
		lsum[i]="__UNK__"

	
	return " ".join(lsum)

if __name__ == "__main__" :
	article= sys.stdin.read() 
	abstractive_summary = abstractive_summarizer(article, word_score_dictionary)
	print(abstractive_summary)
