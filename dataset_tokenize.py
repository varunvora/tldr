import nltk
from pickle import load , dump
from nltk.corpus import stopwords

data_file = open("dataset.pkl", "rb")
x_master, y_master = load(data_file)
del data_file

stop_words = set(stopwords.words('english'))

mytokenizer = nltk.tokenize.RegexpTokenizer(r'\d+\.\d+|[^\W\d]+|\d+')

article_list = []
summary_list = []

for article_x in x_master:
    words = list(filter(lambda x:x not in stop_words , map(lambda y:y.lower() , mytokenizer.tokenize(str(article_x)))))
    article_list.append(words)

for summary_y in y_master:
    words = list(filter(lambda x:x not in stop_words , map(lambda y:y.lower() , mytokenizer.tokenize(str(summary_y)))))
    summary_list.append(words)

print(article_list[0], summary_list[0], sep='\n')
with open('clean_dataset.pkl','wb') as fp :
    dump((article_list,summary_list),fp)