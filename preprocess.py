import pickle
from nltk.tokenize import word_tokenize, sent_tokenize

def pre_aesop_fables() :
	with open("aesop-fables.txt", "r") as infile :
		title = ""
		body = ""
		stories = []
		for line in infile :
			line = line[:-1]
			if line.isupper() :
				if title :
					body = [word_tokenize(word) for word in sent_tokenize(body.lower())]
					stories.append([word_tokenize(title), body])
					body = ""
				title = line
			elif line :
				body = body + ' ' + line
		if title :
			body = [word_tokenize(word) for word in sent_tokenize(body.lower())]
			stories.append([word_tokenize(title), body])

	with open("aesop-fables.pkl", "wb") as fp :
		pickle.dump(stories, fp)

def pre_cnn() :
	with open("cnn_dataset.pkl", "rb") as fp :
		cnn = pickle.load(fp)
	stories = []
	for i in cnn[:10000] :
		story = i['story']
		stories.append([word_tokenize(sentence) for sentence in story])

	with open("cnn.pkl", "wb") as fp :
		pickle.dump(stories, fp)

if __name__ == "__main__" :
	# pre_aesop_fables()
	# with open("aesop-fables.pkl", "rb") as fp :
	# 	stories = pickle.load(fp)
	# print(len(stories))
	# print(stories)

	pre_cnn()
	with open("cnn.pkl", "rb") as fp :
		stories = pickle.load(fp)
	print(stories[0])