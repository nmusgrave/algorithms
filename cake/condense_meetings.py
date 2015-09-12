#! opt/local/bin/python3
import sys

'''
Given: unsorted array of tuples, designating start and end times of meetings.
	Each integer designates number of 30 minute blocks past 9 am.
Produce: array of condensed meetings, should be efficient even if meeting
	times have no upper bound

Follow-up Q:
- What if we did have an upper bound on the input values?
  Could we improve our runtime? Would it cost us memory?
With an upper bound, could create an array of size latest meeting, and
  mark each element as in a meeting or not. Result array would be generated
  from scanning this array and generating tuples to designate the bounds of
  marked time slots.
This gives O(n) runtime, but generates two arrays. Space usage is 
  O(latest meeting)

- Could we do this "in-place" on the input array and save some space?
  What are the pros and cons of doing this in-place?
It is possible to use a swapping sort algorithm to perform the sort in-place,
  and iterate over the array, repeatedly merging adjacent elements.
However, this 
'''

# merge sort customized for pairs, sorting based upon first element in tuple
def merge_halves(target_array, left, right):
	result_array = []
	left_i = 0
	right_i = 0
	while left_i < len(left) and right_i < len(right):
		# sort based upon starting time, first element in tuple
		if left[left_i][0] < right[right_i][0]:
			# first element in left tuple is smaller
			result_array.append(left[left_i])
			left_i += 1
		elif left[left_i][0] is right[right_i][0]:
			# first elements are identical, so insert based upon right element
			if left[left_i][1] < right[right_i][1]:
				result_array.append(left[left_i])
				left_i += 1
			else:
				result_array.append(right[right_i])
				right_i += 1
		else:
			# first element in right tuple is larger
			result_array.append(right[right_i])
			right_i += 1
	# insert any remaining elements
	if left_i < len(left):
		for i in range(left_i, len(left)):
			result_array.append(left[i])
	elif right_i < len(right):
		for i in range(right_i, len(right)):
			result_array.append(right[i])
	return result_array

def merge_sort(array, start, end):
	if end - start < 2:
		return array[start:end];
	middle = start + (int)((end - start) / 2)
	left = merge_sort(array, start, middle)
	right = merge_sort(array, middle, end)
	array = merge_halves(array, left, right)
	return array

def condense_meeting_times(meetings):
	# sort by start time
	meetings = merge_sort(meetings, 0, len(meetings))
	condensed = []
	index = 0
	condensed.append(meetings[index])
	while index < len(meetings):
		if meetings[index][0] > condensed[-1][1]:
			# current meeting starts after running meeting has ended
			condensed.append(meetings[index])
		elif meetings[index][0] <= condensed[-1][1]:
			# current meeting starts during running meeting
			if meetings[index][1] > condensed[-1][1]:
				# current meeting continues beyond running meeting
				# update end time of running meeting
				this_meeting = (condensed[-1][0], meetings[index][1])
				condensed[-1] = this_meeting
		index += 1
	return condensed

def main(argv):
	print('Check sorting of tuples:')
	print(merge_sort( [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], 0, 5 ))
	print(merge_sort( [(5, 4), (5, 3), (5, 2), (5, 6), (4, 2), (3, 1), (6, 9)], 0, 7))
	print('Merge meeting times:')
	print(condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]), ' == [(0, 1), (3, 8), (9, 12)]?')
	print(condense_meeting_times([(0, 1), (1, 2)]), ' == [(0, 2)]?')
	print(condense_meeting_times([(0, 3), (1, 2)]), ' == [(0, 3)]?')
	print(condense_meeting_times([(0, 2), (1, 3)]), ' == [(0, 3)]?')
	print(condense_meeting_times([(1, 10), (2, 6), (3, 5), (7, 9)]), ' == [(1, 10)]?')


if __name__ == '__main__':
	main(sys.argv[1:])