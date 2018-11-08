from nltk.tokenize import sent_tokenize, word_tokenize
import math
import pickle

class ExtractiveSummarizer_tfidf :
	def __init__(self, corpus = "clean_dataset") :
		with open(corpus + ".pkl", "rb") as fp :
			self.corpus, temp = pickle.load(fp)
		self.init_idf()

	def init_idf(self) :
		# number of documents
		N = len(self.corpus)

		# document frequency - number of documents a particular word occurs in.
		df = {}
		for doc in self.corpus :
			for word in doc : #after cleaning there is no such thing as sentence
				#"Vishal is lodu. Kushal is not => [vishal, is, lodu...]
				df[word] = df.get(word, 0) + 1
		self.idf = {x : math.log(N / df[x], 10) for x in df}

	def get_idf(self, word) :
		N = len(self.corpus)
		return self.idf.get(word, math.log(N))

	def tf_idf_summarizer(self, text, sentence_count = 5) :
		if sentence_count <= 0 :
			print("error: sentence_count has to be a positive integer!")

		# preprocess
		sentences = sent_tokenize(text)
		sentences = [word_tokenize(sentence) for sentence in sentences]

		original_sentences = list(sentences)
		sentences = [[word.lower() for word in sentence] for sentence in sentences]

		# number of sentences
		N = len(sentences)

		if sentence_count > N :
			print("error: sentence_count greater that number of sentences in the article!")
			return

		# term frequency - number of times a word occurs in a document.
		tf = {}
		for sentence in sentences :
			for word in sentence :
				if word == '.' or word == ',' or word == '?' or word == '"' or word == '\'' or word == '(' or word == ')' :
					continue
				tf[word] = tf.get(word, 0) + 1

		# sort sentence indices based on tf-idf score
		indices = list(range(N))
		indices.sort(key = lambda i : sum([tf.get(word, 0) * self.get_idf(word) for word in sentences[i]]))
		indices = set(indices[:sentence_count])

		# append highest scoring sentences in order to get the summary
		summary = []
		for i in range(len(original_sentences)) :
			if i in indices :
				summary.append(original_sentences[i])
		summary = " ".join([" ".join(x) for x in summary])
		return summary

if __name__ == "__main__" :
	text = """President Trump lashed out Tuesday at the publication of questions that special counsel Robert S. Mueller III was said to be interested in asking him as part of the Russia probe and possible attempts to obstruct the inquiry.

In a morning tweet, Trump said it was “disgraceful” that the 49 questions were provided to the New York Times, which published them Monday night.

“So disgraceful that the questions concerning the Russian Witch Hunt were ‘leaked’ to the media,” he wrote on Twitter.
It appears that the leak did not come from Mueller’s office. The Times reported that the questions were relayed to Trump’s attorneys as part of negotiations over the terms of a potential interview with the president. The list was then provided to the Times by a person outside Trump’s legal team, the paper said.

In his tweet, Trump also falsely asserts that there are no questions about “Collusion.” Among those is a query about Trump’s knowledge of any outreach by his former campaign chairman Paul Manafort to Russia “about potential assistance to the campaign.” A court filing this month revealed that Mueller had sought authorization to expand his probe into allegations that Manafort “committed a crime or crimes by colluding with Russian government officials.”

Another question asks about Trump’s knowledge of a June 2016 meeting in Trump Tower between his aides and a Russian lawyer who offered politically damaging information on Trump’s Democratic opponent, Hillary Clinton.

And another asks what Trump knew about “Russian hacking, use of social media or other acts aimed at the campaign?”

In his tweet, Trump calls collusion “a phony crime” and repeats his claim that none existed. The president also derides Mueller’s investigation as having “begun with illegally leaked classified information,” adding: “Nice!”"""

	text_summarizer = ExtractiveSummarizer_tfidf(corpus = "clean_dataset")

	summary = text_summarizer.tf_idf_summarizer(text, sentence_count = 5)
	print(summary)