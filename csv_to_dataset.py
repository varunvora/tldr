import pandas as pd
from pickle import dump
from random import randrange
dataset = pd.read_csv("news_summary.csv", encoding = "latin-1")
print(dataset.describe())

x_master = dataset['ctext']
y_master = dataset['text']

del dataset

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




