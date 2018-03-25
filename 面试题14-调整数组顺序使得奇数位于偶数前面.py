# ------- coding:utf-8 ------
'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分
'''

class Solution:
	'''
	自己的解法，主要思路是遍历，遇到偶数就往后放，而且在原位置删除
	'''
	def adjustArrayOddEven(self, array):
		i = 0	# 作为数组的下标
		count = 0 # 用来计算已经检查了数组中的多少个数
		while count < len(array):
			# 偶数，往后放
			if array[i] % 2 == 0:
				tmp = array[i]
				array.remove(array[i])
				array.append(tmp)
			# 奇数，不变
			else:
				i += 1
			count += 1
		return array

	'''
	书上的解法：两个指针一前一后，如果前面指向偶数，后面指向奇数，则交换
	'''
	def adjustArrayOddEven2(self, array):
		left = 0
		right = len(array)-1
		while left < right:
			while array[left]%2==1:
				left += 1
			while array[right]%2==0:
				right -= 1
			if left < right:
				array[left], array[right] = array[right], array[left]
		return array


if __name__ == '__main__':
	s = Solution()
	print s.adjustArrayOddEven([1,2,5,9,7,4,3,6])
	print s.adjustArrayOddEven2([1,2,5,9,7,4,3,6])





