import pandas as pd
from pickle import dump
from random import randrange
dataset = pd.read_csv("news_summary.csv", encoding = "latin-1")
print(dataset.describe())

x = dataset['ctext']
y = dataset['text']
del dataset

invalid_data = 0
x_master, y_master = [], []
for article, summary in zip(x, y) :
	if article and summary and str(article) != "nan" and str(summary) != "nan" and len(article) and len(summary) :
		x_master.append(article)
		y_master.append(summary)
	else :
		invalid_data += 1
del x, y
print("Invalid data:", invalid_data)
print("Dataset Size :",len(x_master), len(y_master))

print("Some random summaries in our dataset")
for i in range(3) :
	temp = randrange(len(x_master))
	print("ARTICLE : ")
	print(x_master[temp])
	print("SUMMARY : ")
	print(y_master[temp])
	print()

data_file = open("dataset.pkl", "wb")
dump((x_master, y_master), data_file)
data_file.close()