#! opt/local/bin/python3
import sys

'''
interviewcake.com

Given: stock prices as array. Indices designate minutes past start of
	trading time. Values are $ of some stock.
Output: best profit from 1 purchase and 1 sale of stock, where purchase
	before sell. Can't buy and sell in same step.
'''

def compute_opt(stock_values):
	if len(stock_values) < 2:
		return 0
	cheapest = stock_values[0]
	profit = stock_values[1] - cheapest
	for i in range(1, len(stock_values)):
		profit = max(profit, stock_values[i] - cheapest)
		cheapest = min(stock_values[i], cheapest)
	return profit

def main(argv):
	stocks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(compute_opt(stocks), ' == 9?')

	stocks = [9, 8, 7, 6, 5, 3, 2, 1, 0]
	print(compute_opt(stocks), ' == -1?')

	stocks = [2, 4, 9, 2, 6, 2, 1, 3]
	print(compute_opt(stocks), ' == 7?')

	stocks = [5, 5, 5, 5, 5]
	print(compute_opt(stocks), ' == 0?')

	stocks = [1, 9, 5, 4, 3, 6, 10]
	print(compute_opt(stocks), ' == 9?')

	stocks = [32, 1, 9, 5, 4, 3, 6, 10]
	print(compute_opt(stocks), ' == 9?')

if __name__ == '__main__':
	main(sys.argv[1:])

