#! opt/local/bin/python3

print('------')
print('Weighted-Interval Scheduling Algorithm')
print('Given:\t\tset of intervals with associated weights')
print('Produce:\tvalid schedule of maximum possible weight')
print('------')
'''
-------------------------------
General Notes
-------------------------------
Can't solve greedily
Sort jobs in order of nondecreasing finish time
p(i) = j, where j is nearest preceeding job that doesn't overlap job i
When examining some optimal schedule, a job n may be in the schedule,
	or a more optimal schedule can be produced from jobs [1, ..., n-1]
Either way, the optimal schedule includes a schedule form jobs [1, ..., p(n)]
Therefore, deciding to include some job j is construed from the relation
	OPT(j) = max(weight(j) + OPT(p(j)), OPT(j - 1))
'''

'''
-------------------------------
Recursive
-------------------------------
Sort intervals in order of nondecreasing finish time
Compute-OPT(j)
	if j is 0
		return 0
	else
		return max(weight(j) + Compute-OPT(p(j)), Compute-OPT(j - 1))

Runtime: exponential. Huge number of subproblems to cover, 
	and lots of redundant computation
'''

def recursive_opt(test_case, preceeding, index, schedule):
	if index is -1:
		# can't go any further
		return 0
	else:
		include = test_case.jobs[index].weight + recursive_opt(test_case, preceeding, preceeding[index], schedule)
		exclude = recursive_opt(test_case, preceeding, index - 1, schedule)
		if max(include, exclude) is include and test_case.jobs[index] not in schedule:
			# insert this job into schedule
			schedule.append(test_case.jobs[index])
		return max(include, exclude)


'''
-------------------------------
Dynamic Programming
-------------------------------
The recursive approach redundantly computes solutions for 0 through n
	unique subproblems
Memoization allows us to store results along the way and check
	if they are already computed.
Runtime: polynomial

	OPT(j) = max(weight(j) + OPT(p(j)), OPT(j - 1))
'''
# stores memoized results
def memoize_opt(test_case):
	memoized = []
	memoized.append(0)
	for index in range(0, len(test_case.jobs)):
		# compute heaviest schedule so far
		include = test_case.jobs[index].weight
		if test_case.preceeding[index] >= 0:
			include += memoized[test_case.preceeding[index] + 1]
		exclude = memoized[index]
		max_weight = max(include, exclude)
		# store result so far
		memoized.append(max_weight)
		# save this job into schedule
	return memoized

def memoize_calculate_schedule(test_case, memoized):
	schedule = []
	index = len(memoized) - 1
	while index >= 0:
		include = test_case.jobs[index - 1].weight + memoized[test_case.preceeding[index - 1] + 1]
		exclude = memoized[index - 1]
		if memoized[index] is include:
			schedule.insert(0, test_case.jobs[index - 1])
			index = test_case.preceeding[index - 1] + 1
		else:
			index -= 1
	return schedule

'''
-------------------------------
Helpers
-------------------------------
'''
def main():
	test_cases = build_test_cases('weighted-interval-sched-test-cases.txt')

	# ----
	# build schedule recursively
	#print('Recursive: runs in exponential time')
	#max_weight = recursive_opt(preceeding, 2, schedule)
	#print_results(max_weight, schedule)

	# ----
	# build schedule with memoization	
	print('Dynamic programming: runs in polynomial time')
	for cur_test_case in test_cases:
		print(len(cur_test_case.jobs), len(cur_test_case.preceeding))
		memoized = memoize_opt(cur_test_case)
		schedule = memoize_calculate_schedule(cur_test_case, memoized)
		print('Expected results:')
		print(cur_test_case)
		print('Actual reslts:')
		print_results(memoized[len(cur_test_case.jobs)], schedule)

def print_results(max_weight, schedule):
	print('Maximum schedule weight ', max_weight)
	for j in schedule:
		print(j)

# gives preceeding job, where preceeding[i] gives latest non-overlapping job
#  that comes before job i
def build_preceeding(jobs, preceeding):
	preceeding.append(-1)
	for i in range(1, len(jobs)):
		j = i - 1
		while j >= 0 and jobs[j].end > jobs[i].start:
			j -= 1
		preceeding.append(j)

# build a collection of test cases indicated by a file
def build_test_cases(file_name):
	test_cases = []
	f = open(file_name, 'r')
	content = []
	content = f.read().splitlines()
	i = 0
	while i < len(content):
		if content[i].startswith('Jobs'):
			# start of a case
			t = test_case(i, content)
			test_cases.append(t)
		i += 1
	f.close()
	return test_cases

# parse 	job descriptions from input
# str:		string at which to stop 
# i:		line in content to start reading at
# content: 	an array of strings to read in
# arr:		array of results, where each element corresponds to a line of content
def parser(str, i, content, arr):
	temp_nums = []
	i += 1
	while i < len(content) and not content[i].startswith(str) and len(content[i]) > 0:
		temp_nums = [int(j) for j in content[i].split()]
		temp_job = job(i, temp_nums[0], temp_nums[1], temp_nums[2])
		arr.append(temp_job)
		i += 1
	return i

# job indices start at 0
class job:
	def __init__(self, i, w, s, e):
		self.index = i
		self.weight = w
		self.start = s
		self.end = e
	def __str__(self):
		result = 'weight ' + str(self.weight)
		result += ': [' + str(self.start) + '-' + str(self.end) + ']'
		return result

# store important information for each test case: the jobs to schedule,
# and the resulting maximum-weight schedule
class test_case:
	def __init__(self, i, content):
		self.jobs = []
		i = parser('Expected Results', i, content, self.jobs)
		self.expected_results = []
		i = parser('Jobs', i, content, self.expected_results)
		i += 1
		self.preceeding = []
		build_preceeding(self.jobs, self.preceeding)
	def __str__(self):
		result = 'Jobs:\n'
		for j in self.jobs:
			result += '\t' + str(j) + '\n'
		result += 'Expected Results:\n'
		for r in self.expected_results:
			result += '\t' + str(r) + '\n'
		return result

if __name__ == '__main__':
	main()