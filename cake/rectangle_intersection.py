#! opt/local/bin/python3
import sys
import unittest

'''
Given: two rectangles, with straight edges
Output: rectangle representing overlapping region
'''

def intersector(rectangle_1, rectangle_2):
	left_side = max(rectangle_1['x'], rectangle_2['x'])
	right_side = min(rectangle_1['x'] + rectangle_1['width'], rectangle_2['x'] + rectangle_2['width'])
	bottom_side = max(rectangle_1['y'], rectangle_2['y'])
	top_side = min(rectangle_1['y'] + rectangle_1['height'], rectangle_2['y'] + rectangle_2['height'])
	result = {
		# bottom left corner
		'x': left_side,
		'y': bottom_side,
		# width and height
		'width': right_side - left_side,
		'height': top_side - bottom_side
	}

	if result['width'] <= 0 or result['height'] <= 0:
		result['height'] = 0
		result['width'] = 0
	return result


class TestIntersector(unittest.TestCase):
	def test_no_overlap(self):
		rectangle_1 = {
			# bottom left corner
			'x': 1,
			'y': 5,
			# width and height
			'width': 10,
			'height': 4
		}
		rectangle_2 = {
			# bottom left corner
			'x': 6,
			'y': 10,
			# width and height
			'width': 4,
			'height': 9
		}
		result = intersector(rectangle_1, rectangle_2)

		self.assertEqual(result['width'], 0)
		self.assertEqual(result['height'], 0)

	def test_overlap_right_aligned(self):
		rectangle_1 = {
			# bottom left corner
			'x': 1,
			'y': 5,
			# width and height
			'width': 10,
			'height': 4
		}
		rectangle_2 = {
			# bottom left corner
			'x': 6,
			'y': 7,
			# width and height
			'width': 4,
			'height': 9
		}
		self.assertEqual(intersector(rectangle_1, rectangle_2), {'x': 6, 'width': 4, 'y': 7, 'height': 2})

	def test_no_overlap_vertical_aligned(self):
		rectangle_1 = {
			# bottom left corner
			'x': 1,
			'y': 5,
			# width and height
			'width': 10,
			'height': 4
		}
		rectangle_2 = {
			# bottom left corner
			'x': 6,
			'y': 9,
			# width and height
			'width': 4,
			'height': 9
		}
		self.assertEqual(intersector(rectangle_1, rectangle_2), {'x': 6, 'width': 0, 'y': 9, 'height': 0})

	def test_overlap_left_right_aligned(self):
		rectangle_1 = {
			# bottom left corner
			'x': 1,
			'y': 5,
			# width and height
			'width': 3,
			'height': 1
		}
		rectangle_2 = {
			# bottom left corner
			'x': 1,
			'y': 1,
			# width and height
			'width': 3,
			'height': 5
		}
		self.assertEqual(intersector(rectangle_1, rectangle_2), {'x': 1, 'width': 3, 'y': 5, 'height': 1})


if __name__ == '__main__':
	unittest.main()
