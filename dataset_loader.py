#CODE TO LOAD THE DATASET :
from pickle import load
from random import randrange
data_file = open("dataset.pkl", "rb")
x_master, y_master = load(data_file)
del data_file

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

