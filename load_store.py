''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

# Write code here
	tree = {} 
	n = int(input())
	a = list(map(int, input().split()))
	x = int(input())
	for i in range(n) :
		if a[i] not in tree :
			tree[a[i]] = [i]
		else :
			tree[a[i]].append(i)
	def delete_node(x) :
		if x in tree :
			children = tree[x]
			del tree[x]
			for child in children :
				delete_node(child)
		for parent in tree :
			if x in tree[parent] :
				tree[parent].remove(x)
	# print(tree)
	delete_node(x)
	# print(tree)
	leaves = 0
	for node in sum(list(tree.values()), []) :
		if node not in tree or (node in tree and tree[node] == []):
			# print(node)
			leaves += 1
	print(leaves)
	#print(tree)



main()

