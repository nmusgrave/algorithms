#! opt/local/bin/python3
from collections import deque
import sys

print("------")
print("Gale-Shapely Algorithm")
print("Premise: \n\tThere exists a stable matching for every set of prefence lists between men and women.")
print("(simplified for marriages, but also applies to more general case of companies and applicants, where each company can accept multiple applicants, and each applicant goes to one company)");
print("Given:\n\tpreferences between n women and n men")
print("Produce:")
print("\t- Assignment of women and men such that a stable matching")
print("\tis formed. ")
print("\t- To be a stable matching, no pair can prefer each other to ")
print("\tcurrent partners.")
print("\tUnstable: m-w, m'-w', where m prefers w', and w' prefers m")
print("\t- A perfect matching has each in one pair.")
print("\t- Completed in at worst O(n^2) time")
print("------")

'''
-------------------------------
Algorithm
-------------------------------
set E of employers
set A of applicants

where there exists an E with no employee yet
	choose E
	let A be highest-ranked applicant that E has not yet extended offer to
	if A is free, then
		E, A are matched
	else A is working for E'
		if A prefers E'
			E is still searching for employee
		else
			E, A are matched
			E' is free
return pairs

Keep track of free men
	linked list of free men
Keep track of each man's preferences
	man_preference[m][i] gives ith prefered woman for man m
O(1) access to next woman on some man's preference list
	next_proposal[i] = j gives woman j next on preference list, for man i
O(1) check if woman is free
	woman[i] gives partner/null
O(1) check which partner a woman prefers
	array of arrays, where woman_preference[w][m] gives ranking of 
	man m for woman w
Note: does not need to be symmetric data structure for men and women!
'''
def match_stable(n, man_preference, woman_preference):
	# list of unmarried men
	free_men = deque([x for x in range(n)])

	# gives woman j next on ith man's preference list
	# array of integers, initialized to 0 to start with first preference
	next_proposal = [0 for x in range(n)]

	# engagement partner/status for each woman, where non-positive
	#	integer denotes unmarried
	# all are initially unmarried
	woman_status = [-1 for x in range(n)]

	while len(free_men) > 0:
		current_man = free_men.popleft()
		woman_index = next_proposal[current_man]
		next_woman = man_preference[current_man][woman_index]
		if woman_status[next_woman] < 0:
			# available to marry
			woman_status[next_woman] = current_man
		else:
			# get previous match
			old_man = woman_status[next_woman]
			# must check if current matching is stable, or new matching is better
			# if woman ranks previous (low num) below this man (high num)
			if woman_preference[next_woman][old_man] > woman_preference[next_woman][current_man]:
				# woman prefers new man to previous match
				woman_status[next_woman] = current_man
				free_men.append(old_man)
			else:
				# woman prefers previous match, so this man needs to keep looking
				free_men.append(current_man)
				# move on to examining the next woman for this man
		woman_index += 1
		next_proposal[current_man] = woman_index;
	return woman_status

''' 
-------------------------------
process input files, run test cases
-------------------------------
'''
def pref_helper(str, i, content, arr):
	temp = []
	i += 1
	while(i < len(content) and not content[i].startswith(str) and len(content[i]) > 0):
		temp = [int(j) for j in content[i].split()]
		temp.pop(0)
		arr.append(temp)
		i += 1
	return i

class test_case:
	def __init__(self, i, content):
		self.man_preference = []
		i = pref_helper("Women", i, content, self.man_preference)
		self.woman_preference = []
		i = pref_helper("Expected Results", i, content, self.woman_preference)
		i += 1
		self.woman_results = []
		self.woman_results = [int(j) for j in content[i].split()]
		#i = builder_helper("Men", i, content, self.woman_results)
		self.pairs = len(self.woman_results)
	def __str__(self):
		result = "Men\n" + str(self.man_preference)
		result += "\nWomen\n" + str(self.woman_preference)
		result += "\nExpected Results\n" + str(self.woman_results)
		return result

def build_test_cases(file_name):
	test_cases = []
	f = open(file_name, "r")
	content = []
	content = f.read().splitlines()
	i = 0
	while i < len(content):
		if(content[i].startswith("Men")):
			# start of a case
			t = test_case(i, content)
			test_cases.append(t)
		i += 1
	f.close()
	return test_cases

def main(argv):
	test_cases = []
	if len(argv) < 2:
		print("Running default test cases file")
		# TODO remove hard coding
		test_cases = build_test_cases("stable-matching-test-cases.txt");
	else:
		for arg in argv:
			print("Running on file ", arg)
			test_cases += build_test_cases(file_name)

	woman_status = []
	for t in test_cases:
		woman_status = match_stable(t.pairs, t.man_preference, t.woman_preference)
		print("Result: ")
		print(woman_status)
		print("Expected: ")
		print(t.woman_results)
		for w in range(t.pairs):
			assert woman_status[w] == t.woman_results[w]

if __name__ == "__main__":
	main(sys.argv[1:])

