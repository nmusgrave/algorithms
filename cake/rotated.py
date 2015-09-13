#! opt/local/bin/python3
import sys

'''
Given huge array of words, find rotation point.
Array is sorted, but has been shifted so start of sorted section is
not at the front.
'''

def find_rotation_point_iterative(arr, lower, upper):
	while lower <= upper:
		partition = (int)((upper + lower + 1) / 2)
		if partition - 1 >= 0 and arr[partition] < arr[partition - 1]:
			return partition
		if arr[lower] < arr[partition]:
			# subsection is sorted, so examine upper half
			lower = partition + 1
		elif arr[partition] <= arr[upper]:
			# subsection is sorted, so examine lower half
			upper = partition - 1
	if arr[0] < arr[len(arr) - 1]:
		return 0
	return partition

def find_rotation_point_helper(arr, lower, upper):
	if lower > upper:
		return -1;
	partition = (int)((lower + upper + 1) / 2)
	if partition - 1 >= 0 and arr[partition] < arr[partition - 1]:
		return partition
	if arr[lower] < arr[partition]:
		# subsection is sorted, so examine upper half
		return find_rotation_point_helper(arr, partition + 1, upper)
	elif arr[partition] <= arr[upper]:
		# subsection is sorted, so examine lower half
		return find_rotation_point_helper(arr, lower, partition - 1)

def find_rotation_point_runner(arr, expected):
	if arr[0] <= arr[len(arr) - 1]:
		result = 0
	else:
		result = find_rotation_point_helper(arr, 0, len(arr) - 1)
	print('Recursive: ', result, ' == ', expected, '?')
	result = find_rotation_point_iterative(arr, 0, len(arr) - 1)
	print('Iterative: ', result, ' == ', expected, '?')	


# true if value may potentially be within these bounds
# either because segment is sorted, and falls within range,
# or segment contains rotated point and target may still be in
# this range
def within_rotated_segment(arr, lower, upper, target):
	return (arr[lower] <= arr[upper] and target >= arr[lower] and target <= arr[upper]) or \
		(arr[lower] > arr[upper] and (target >= arr[lower] or target <= arr[upper]))

def search_rotated_arr(arr, target):
	lower = 0
	upper = len(arr) - 1
	while lower < upper:
		partition = (int)((lower + upper + 1) / 2)
		if target is arr[partition]:
			return partition
		if within_rotated_segment(arr, lower, partition - 1, target):
			upper = partition - 1
		else:
			lower = partition + 1
	if arr[upper] is target:
		return upper

def main(argv):
	words = [
		'asymptote', # <-- rotates here!
		'babka',
		'banoffee',
		'engender',
		'karpatka',
		'othellolagkage',
		'ptolemaic',
		'retrograde',
		'supplant',
		'undulate',
		'xenoepist',
	]
	find_rotation_point_runner(words, 0)
	print(search_rotated_arr(words, 'asymptote'), '\t== 0?')
	print(search_rotated_arr(words, 'retrograde'), '\t== 7?')
	print(search_rotated_arr(words, 'xenoepist'), '\t== 10?')

	words = [
		'ptolemaic',
		'retrograde',
		'supplant',
		'undulate',
		'xenoepist',
		'asymptote', # <-- rotates here!
		'babka',
		'banoffee',
		'engender',
		'karpatka',
		'othellolagkage',
	]
	find_rotation_point_runner(words, 5)
	print(search_rotated_arr(words, 'asymptote'), '\t== 5?')
	print(search_rotated_arr(words, 'retrograde'), '\t== 1?')
	print(search_rotated_arr(words, 'xenoepist'), '\t== 4?')
	print(search_rotated_arr(words, 'karpatka'), '\t== 9?')

	words = [
		'babka',
		'banoffee',
		'engender',
		'karpatka',
		'othellolagkage',
		'ptolemaic',
		'retrograde',
		'supplant',
		'undulate',
		'xenoepist',
		'asymptote' # <-- rotates here!
	]
	find_rotation_point_runner(words, 10)
	print(search_rotated_arr(words, 'asymptote'), '\t== 10?')
	print(search_rotated_arr(words, 'retrograde'), '\t== 6?')
	print(search_rotated_arr(words, 'xenoepist'), '\t== 9?')
	print(search_rotated_arr(words, 'karpatka'), '\t== 3?')


if __name__ == '__main__':
	main(sys.argv[1:])