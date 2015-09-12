#! opt/local/bin/python3
import sys

'''
Given: amount of money, and list of coin denominations
Output: number of ways to make change
'''

def recursive_combinations(target, coin_index, denominations):
	if target is 0:
		return 1
	elif target < 0 or coin_index < 0:
		return 0
	ways = recursive_combinations(target, coin_index - 1, denominations)
	ways += recursive_combinations(target - denominations[coin_index], coin_index, denominations)
	return ways

def memoize_combinations(target, denominations):
	counts = [[0 for x in range(len(denominations))] for x in range(target + 1)]
	for i in range(0, len(counts)):
		for j in range(len(counts[i])):
			if i is 0:
				counts[i][j] = 1
			elif i < 0 or j < 0:
				counts[i][j] = 0
			elif denominations[j] > i:
				counts[i][j] = counts[i][j - 1]
			else:
				counts[i][j] = counts[i][j - 1] + counts[i - denominations[j]][j]
	return counts[target][len(denominations) - 1]

def small_memoize_combinations(target, denominations):
	counts = [0 for x in range(target + 1)]
	counts[0] = 1
	for i in range(len(denominations)):
		for j in range(denominations[i], target + 1):
			counts[j] += counts[j - denominations[i]]
	return counts[target]

def main(argv):
	target = 4
	print(recursive_combinations(4, 2, [1, 2, 3]), ' == 4?')
	print(memoize_combinations(4, [1, 2, 3]), ' == 4?')
	print(memoize_combinations(9, [1, 2, 3]), ' == 12?')
	print(small_memoize_combinations(4, [1, 2, 3]), ' == 4?')
	print(small_memoize_combinations(8, [1, 2, 3]), ' == 10?')


if __name__ == '__main__':
	main(sys.argv[1:])