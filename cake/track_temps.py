#! opt/local/bin/python3
import sys

'''
class TempTracker
	int insert(int) record new temp
	int get_max() hotest seen so far
	int get_min() lowest seen so far
	float get_mean()
	int get_mode()
optimize for space and time, favoring get over insert
temps all in Fahrenheit, range 0 - 110
'''
class TempTracker:
	def __init__(self):
		self.num_temps = 0
		self.running_sum = 0
		self.min = -1
		self.max = -1
		# since range end is exclusive
		self.temp_counter = [0 for x in range(111)]
		self.mode = -1
		print(len(self.temp_counter))

	def insert(self, temp):
		print(temp)
		self.temp_counter[temp] += 1
		if self.temp_counter[temp] > self.temp_counter[self.mode]:
			self.mode = temp
		self.num_temps += 1
		self.running_sum += temp
		if self.min < 0:
			self.min = temp
		else:
			self.min = min(self.min, temp)
		if self.max < 0:
			self.max = temp
		else:
			self.max = max(self.max, temp)

	def get_max(self):
		return self.max

	def get_min(self):
		return self.min

	def get_mean(self):
		return self.running_sum / self.num_temps

	def get_mode(self):
		return self.mode

def main(argv):
	t = TempTracker()
	temps = [5, 9, 13, 89, 65, 4, 67, 54, 54, 67, 54]
	for num in temps:
		t.insert(num)
	print(t.get_min(), t.get_max(), t.get_mean(), t.get_mode())


if __name__ == '__main__':
	main(sys.argv[1:])