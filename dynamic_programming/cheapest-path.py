#! opt/local/bin/python3
import sys
import copy

print('------')
print('Cheapest Path')
print('Given:\nAn integer tree, where the first row has 1 element,\nthe second has 2, the third has 3, etc.')
print('Produce:\nThe cheapest path from root to bottom row, summing\nalong node values between parents and children.')
print('------')


'''
-------------------------------
Algorithm
-------------------------------
     5
    9 1
   2 7 8
  0 3 6 5

while haven't processed root
	for node in level
		cheapest path through node is node.value + 
			min(left child path, right child path)

If levels are 1 through n, and the ith level has i elements
for node at level i, position j:
	left child is at level i + 1, position j
	right child is at level i + 1, position j + 1
'''

def calculate_cost(tree):
	cost = []
	# store costs in structure with same dimensions as tree
	for r in range(len(tree)):
		cost.append([])
		for e in range(len(tree[r])):
			cost[r].append(tree[r][e])
	# skip processing bottom row, since their costs are just the
	# value of that element
	row = len(tree) - 2
	while row >= 0:
		element = 0
		while element < len(tree[row]):
			left_cost = tree[row][element] + cost[row + 1][element]
			right_cost = tree[row][element] + cost[row + 1][element + 1]
			cost[row][element] = min(left_cost, right_cost)
			element += 1
		row -= 1
	return cost

# if multiple possible paths exist, generates one
def discover_path(tree, cost):
	path = []
	row = 0
	element = 0
	while row < len(tree) - 1:
		print(tree[row], cost[row + 1])
		left_cost = tree[row][element] + cost[row + 1][element]
		right_cost = tree[row][element] + cost[row + 1][element + 1]
		if cost[row][element] is left_cost:
			path.append('L')
		else:
			element += 1
			path.append('R')
		row +=1
	return path

def print_results(tree, expected_cost):
	print('Tree:')
	print(tree)
	print('Expected costs:')
	print(expected_cost)
	print('Actual costs:')
	cost = calculate_cost(tree)
	print(cost)
	print('Path from root to bottom:')
	path = discover_path(tree, cost)
	print(path)

def main(argv):
	trees = (
	  ( [5],
	   [9, 1],
	  [2, 7, 8],
	 [0, 3, 6, 5] ),
	  ( [5],
	   [11, 1],
	  [2, 7, 8],
	 [0, 3, 6, 5] ) )

	expected_costs = (
	   ( [16],
	   [11, 11],
	  [2, 10, 13],
	 [0, 3, 6, 5] ),
	    ( [16],
	   [13, 11],
	  [2, 10, 13],
	 [0, 3, 6, 5] ) )

	for i in range(0, len(trees)):
		print_results(trees[i], expected_costs[i])


if __name__ == '__main__':
	main(sys.argv[1:])