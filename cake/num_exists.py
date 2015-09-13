#! opt/local/bin/python3
import sys

'''
Given array of n sorted integers.
Quickly determine if given integer is in array.
'''
def does_num_exist(arr, target, lower, upper):
	if lower > upper:
		return False
	partition = (int)((upper + lower) / 2)
	if arr[partition] is target:
		return True;
	elif lower is upper:
		return False;
	elif arr[partition] > target:
		return does_num_exist(arr, target, lower, partition - 1)
	else:
		return does_num_exist(arr, target, partition + 1, upper)

def main(argv):
	arr = [1, 2, 3]
	print(does_num_exist(arr, 1, 0, len(arr) - 1), ' == True?')
	print(does_num_exist(arr, 2, 0, len(arr) - 1), ' == True?')
	print(does_num_exist(arr, 3, 0, len(arr) - 1), ' == True?')
	print(does_num_exist(arr, 0, 0, len(arr) - 1), ' == False?')
	print(does_num_exist(arr, 4, 0, len(arr) - 1), ' == False?')

	arr = [0, 3, 5, 9]
	print(does_num_exist(arr, 0, 0, len(arr) - 1), ' == True?')
	print(does_num_exist(arr, 5, 0, len(arr) - 1), ' == True?')
	print(does_num_exist(arr, 6, 0, len(arr) - 1), ' == False?')
	print(does_num_exist(arr, 2, 0, len(arr) - 1), ' == False?')

if __name__ == '__main__':
	main(sys.argv[1:])