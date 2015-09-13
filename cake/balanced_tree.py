#! opt/local/bin/python3
from collections import deque
import sys

'''
Determine if binary tree is superbalanced (difference between
	any two nodes is no more than 1)
'''

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def is_superbalanced(self):
		# quit when find more than 2 depths
		depths = []
		# store node, depth tuples
		stack = []
		stack.append((self, 0))
		while len(stack):
			cur_node, depth = stack.pop()
			if cur_node.left is None and cur_node.right is None:
				# found a leaf
				if depth not in depths:
					depths.append(depth)
					if len(depths) > 2 or \
						(len(depths) is 2 and abs(depths[0] - depths[1]) > 1):
						return False
			else:
				# not a leaf, continue traversing
				if cur_node.left:	
					stack.append((cur_node.left, depth + 1))
				if cur_node.right:
					stack.append((cur_node.right, depth + 1))
		if len(depths) is 1 and depths[0] > 1:
			return False
		return True


def main(argv):
	'''
		5
	10		11
	3
	4
	'''
	n = Node(5)
	n.left = Node(10)
	n.right = Node(11)
	n.left.left = Node(3)
	print(n.is_superbalanced(), ' == True?')
	n.left.left.right = Node(4)
	print(n.is_superbalanced(), ' == False?')

	'''
		4
	5
	9
	'''
	n2 = Node(4)
	n2.left = Node(5)
	print(n2.is_superbalanced(), ' == True?')
	n2.left.left = Node(9)
	print(n2.is_superbalanced(), ' == False?')



if __name__ == '__main__':
	main(sys.argv[1:])