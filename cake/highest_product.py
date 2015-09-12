#! opt/local/bin/python3
import sys
import queue

'''
Given: array of integers
Produce: highest product from 3 of the elements
'''

# to protect against integer overflow when computing product, should
# use large integer data type
def highest_product_from_three(nums):
	if len(nums) < 3:
		return -1;
	# initialize to hold the first 3 elements
	max_three = queue.PriorityQueue(3)
	highest_so_far = 1
	for i in range(3):
		highest_so_far *= nums[i]
		max_three.put(nums[i])

	for i in range(3, len(nums)):
		potential_product = max_three.queue[1] * max_three.queue[2] * nums[i]
		print(i, potential_product, highest_so_far)
		if potential_product > highest_so_far:
			max_three.get(0)
			max_three.put(nums[i])
			highest_so_far = nums[i]

	return max_three.queue[0] * max_three.queue[1] * max_three.queue[2]

def main(argv):
	print(highest_product_from_three([0, 0]), ' == -1?')
	print(highest_product_from_three([2, 3, 4, 5]), ' == 60?')
	print(highest_product_from_three([5, 2, 4, 3]), ' == 60?')
	print(highest_product_from_three([1, 2, 6, 5, 9]), ' == 270?')
	print(highest_product_from_three([1, 9, 2, 6, 5]), ' == 270?')
	print(highest_product_from_three([1, 1, 1, 1, 1]), ' == 1?')
	print(highest_product_from_three([-1, -3, -6, -8, -10]), ' == -18?')
	print(highest_product_from_three([-1, -3, -6, -8, 10]), ' == 30?')
	print(highest_product_from_three([-10, -10, 1, 3, 2]), ' == 300?')

if __name__ == '__main__':
	main(sys.argv[1:])