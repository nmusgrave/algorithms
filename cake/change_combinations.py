#! opt/local/bin/python3
import sys

'''
Given: amount of money, and list of coin denominations
Output: number of ways to make change
'''

def compute_combinations(target, denominations):
	# ith element has number of ways to give i in change
	combinations = [0] * (target + 1)
	for coin in denominations:
		if coin < target:
			combinations[coin] = 1
	for i in range(1, target + 1):
		for coin in denominations:
			if i - coin >= 0:
				print('here', i, i - coin)
				combinations[i] += combinations[i - coin]
			print(i, coin, combinations)
	return combinations

def main(argv):
	print(compute_combinations(4, [1, 2, 3]), ' == 4?')

'''
	1 1 1 1 1
	1 1 2 1
	1 3 1
	2 2 

	3 2

	0 1 2 3 4 
'''
if __name__ == '__main__':
	main(sys.argv[1:])