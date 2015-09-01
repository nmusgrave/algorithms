#! opt/local/bin/python3
import sys

'''
interviewcake.com

Given: an array of ints
Output: an array of results, where each index corresponds to
	the product of every int except that one
Do not use division.
'''

def compute_products(array):
	# build of array of product of all numbers in [0, i)
	preceeding_products = []
	preceeding_products.append(1)
	for i in range(1, len(array)):
		preceeding_products.append(preceeding_products[i - 1] * array[i - 1])

	# build array of product of all numbers (i, len(array))
	following_products = []
	following_products.append(1)
	for i in range(1, len(array)):
		following_products.insert(0, following_products[0] * array[len(array) - i])

	# combine results
	total_products = []
	for i in range(0, len(array)):
		total_products.append(preceeding_products[i] * following_products[i])
	
	return total_products


def main(argv):
	print(compute_products([2, 3, 4, 5]))
	print(compute_products([1, 2, 6, 5, 9]))
	print(compute_products([1, 1, 1, 1, 1]))
	print(compute_products([0, 0]))


if __name__ == '__main__':
	main(sys.argv[1:])



