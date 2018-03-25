# -------coding:utf-8---------
'''
题目：请实现一个函数，输入一个整数，输出该数二进制表述中1的个数。
例如，把9表示成二进制1001，有两位是1。因此如果输入是9，则该函数输出为2.
'''

class Solution:
	def count(self, n):
		c = 0
		while n > 0:
			if n % 2 == 1:
				c += 1
			n /= 2
		return c

if __name__ == '__main__':
	s = Solution()
	print s.count(9)
	


