#CODE TO LOAD THE DATASET :
from pickle import load
from random import randrange
import numpy as np
from sklearn.model_selection import train_test_split

def load_dataset(split = False, split_ratio = 0.7) :
	data_file = open("dataset.pkl", "rb")
	x_master, y_master = load(data_file)
	data_file.close()
	if not split :
		return x_master, y_master
	else :
		x_master = np.array(x_master)
		y_master = np.array(y_master)
		x_train, x_test, y_train, y_test = train_test_split(x_master, y_master, train_size = split_ratio, shuffle = True)
		return list(x_train), list(x_test), list(y_train), list(y_test)

if __name__=="__main__":
	x_master, y_master = load_dataset()
	#Verification
	print("Size of X : ", len(x_master))
	print("Size of Y : ", len(y_master))

	print("Some random summaries in our dataset")
	for i in range(3) :
		temp = randrange(len(x_master))
		print("ARTICLE : ")
		print(x_master[temp])
		print("SUMMARY : ")
		print(y_master[temp])
		print()
