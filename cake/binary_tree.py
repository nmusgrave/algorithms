#! opt/local/bin/python3
import sys

'''
1)
Determine if binary tree is superbalanced (difference between
	any two nodes is no more than 1)

2)
Determine if binary tree is valid binary search tree
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

	def is_bst(self):
		stack = []
		stack.append((sys.maxsize + 1, self, sys.maxsize))
		while len(stack):
			lower_limit, cur_node, upper_limit = stack.pop()
			if cur_node.left:
				if cur_node.left.value < cur_node.value and cur_node.left.value > lower_limit:
					stack.append((lower_limit, cur_node.left, cur_node.value))
				else:
					return False
			if cur_node.right:
				if cur_node.right.value >= cur_node.value and cur_node.right.value <= upper_limit:
					stack.append((cur_node.value, cur_node.right, upper_limit))
				else:
					return False
		return True

	# only for BST
	def get_largest(self):
		cur_node = self
		while cur_node.right:
			cur_node = cur_node.right
		return cur_node.value

	# only for BST
	# second largest is parent of rightmost leaf
	def get_second_largest(self):
		cur_node = self
		while cur_node is not None:
			# parent of right leaf
			if cur_node.right and not cur_node.right.left and not cur_node.right.right:
				return cur_node.value
			# no right children, so find largest in left subtree
			if not cur_node.right:
				return cur_node.left.get_largest()
			cur_node = cur_node.right
		return cur_node.value

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
	print(n.is_bst(), ' == False?')

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
	print(n2.is_bst(), ' == False?')

	'''
			5
		3		5
	2	  4	   		6
						8
					7		9
	'''
	n3 = Node(5)
	print(n3.is_bst(), ' == True?')
	n3.left = Node(3)
	n3.left.left = Node(2)
	print(n3.is_bst(), ' == True?')
	n3.left.right = Node(4)
	print(n3.is_bst(), ' == True?')
	n3.right = Node(5)
	print(n3.is_bst(), ' == True?')
	n3.right.right = Node(6)
	print(n3.is_bst(), ' == True?')
	n3.right.right.right = Node(8)
	print(n3.is_bst(), ' == True?')
	n3.right.right.right.left = Node(7)
	print(n3.is_bst(), ' == True?')
	n3.right.right.right.right = Node(9)
	print(n3.is_bst(), ' == True?')

	print(n3.get_second_largest(), ' == 8?')


	'''
			5
		3		5
	2	  6	   		6
						8
					7		9
	'''
	n3.left.right.value = 6
	print(n3.is_bst(), ' == False?')


	'''
			5
		3		5
	2	  4	   		6
						10
					7
					  8
	'''
	n3.left.right.value = 4
	n3.right.right.right = Node(10)
	n3.right.right.right.left = Node(7)
	n3.right.right.right.left.right = Node(8)
	print(n3.get_second_largest(), ' == 8?')



if __name__ == '__main__':
	main(sys.argv[1:])