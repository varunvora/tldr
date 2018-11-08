import pickle
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

stopwords = set(stopwords.words('english'))


class ExtractiveSummarizer_bayes :
    def __init__(self, corpus = "clean_dataset") :
        with open(corpus + ".pkl", "rb") as fp :
            self.article_word_list, self.summary_word_list = pickle.load(fp)
        self.word_score_dict = self.get_word_score(self.article_word_list, self.summary_word_list)

#this is better
#in face there should be one summarizer class and these 2 should inherit from it
    #true
    #and only one overloaded summarise() function yeah, but for AIR its enough no? yeah, i guess
    #i'll push this

    def get_word_score(self, article_word_list, summary_word_list):
        Na = len(article_word_list)  # total number of words in the articles
        Ns = len(summary_word_list)  # total number of words in the summaries

        article_word_dict = Counter(sum(article_word_list, []))
        summary_word_dict = Counter(sum(summary_word_list, []))
        combined_dict = article_word_dict + summary_word_dict

        Va = len(article_word_dict)  # number of unique words in the articles
        Vs = len(summary_word_dict)  # number of unique words in the summaries

        # P(Wi | Sw)
        P_Wi_given_Sw = Counter({word: summary_word_dict[word] / Ns for word in summary_word_dict})
        # P(Sw)
        P_Sw = Ns / (Na + Ns)
        # P(Wi)
        P_Wi = Counter({word: (combined_dict[word]) / (Na + Ns) for word in combined_dict})
        # P(Sw | Wi)
        word_score_dict = Counter({word: P_Wi_given_Sw[word] * P_Sw / P_Wi[word] for word in article_word_dict})
        return word_score_dict


    def sentence_score(self, sentence):
        context_words = [word for word in word_tokenize(sentence) if word not in stopwords and len(word) > 1]
        return sum([self.word_score_dict[word] for word in context_words]) / (len(context_words) + 0.01)

    def bayes_summarizer(self, text, sentence_count = 5):
        sentences = sent_tokenize(text)
        sentences.sort(key=lambda x: self.sentence_score(x), reverse=True)
        chosen_sentences = set(sentences[:sentence_count])
        summary = [sentence for sentence in sent_tokenize(text) if sentence in chosen_sentences]
        summary = " ".join(summary).split()
        return " ".join(summary)

# i think you should pickle word_score_dict also.
if __name__ == "__main__" :
    text = """President Trump lashed out Tuesday at the publication of questions that special counsel Robert S. Mueller III was said to be interested in asking him as part of the Russia probe and possible attempts to obstruct the inquiry.

In a morning tweet, Trump said it was “disgraceful” that the 49 questions were provided to the New York Times, which published them Monday night.

“So disgraceful that the questions concerning the Russian Witch Hunt were ‘leaked’ to the media,” he wrote on Twitter.
It appears that the leak did not come from Mueller’s office. The Times reported that the questions were relayed to Trump’s attorneys as part of negotiations over the terms of a potential interview with the president. The list was then provided to the Times by a person outside Trump’s legal team, the paper said.

In his tweet, Trump also falsely asserts that there are no questions about “Collusion.” Among those is a query about Trump’s knowledge of any outreach by his former campaign chairman Paul Manafort to Russia “about potential assistance to the campaign.” A court filing this month revealed that Mueller had sought authorization to expand his probe into allegations that Manafort “committed a crime or crimes by colluding with Russian government officials.”

Another question asks about Trump’s knowledge of a June 2016 meeting in Trump Tower between his aides and a Russian lawyer who offered politically damaging information on Trump’s Democratic opponent, Hillary Clinton.

And another asks what Trump knew about “Russian hacking, use of social media or other acts aimed at the campaign?”

In his tweet, Trump calls collusion “a phony crime” and repeats his claim that none existed. The president also derides Mueller’s investigation as having “begun with illegally leaked classified information,” adding: “Nice!”"""

    text_summarizer = ExtractiveSummarizer_bayes(corpus = "clean_dataset")

    summary = text_summarizer.bayes_summarizer(text, sentence_count = 5)
    print(summary)