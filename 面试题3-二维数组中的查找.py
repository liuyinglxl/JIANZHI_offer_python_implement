# ------coding:utf-8--------
"""
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

import sys
import numpy as np

class Solution:
	"""
	自己想的方法：现在第一列中寻找一个合适的位置，再在这个行中进行查找
	"""
	def find(self, array, num):
		row_len = len(array[0])
		front = array[0][0]
		target_row = -1
		for i in range(1, row_len):
			if num >= front and num < array[0][i]:
				target_row = i-1
		if target_row == -1:
			target_row = row_len
		front = array[target_row][0]
		col_len = len(array[:,0])
		for i in range(0, col_len):
			if array[target_row][i] == num:
				return True
		return False

	"""
	剑指 offer的方法：从右上角开始查找，如果当前值<目标值，则往下移动一行
	如果当前值>目标值，则往左移动一行
	"""
	def find2(self, array, num):
		row = len(array)
		col = len(array[0])
		i = 0
		j = col-1
		while i < row and j >=0:
			if array[i][j] < num:
				i += 1
			elif array[i][j] > num:
				j -= 1
			else:
				return True
		return False

if __name__ == '__main__':
	array = np.array([[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]])
	s = Solution()
	print s.find(array, 7)
	print s.find2(array, 7)



