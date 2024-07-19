def NumsTransform(path_nums):
	with open(path_nums) as f:
		nums = f.readlines()
		numbers = [int(num) for num in nums]
		numbers.sort()
		median = len(numbers) // 2
	print(sum(abs(n - numbers[median]) for n in numbers))

import sys
if __name__ == '__main__':
	path_nums = sys.argv[1]
	NumsTransform(path_nums)