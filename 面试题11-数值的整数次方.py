# --------- coding:utf-8 ---------
'''
题目：实现函数power(base, exponent)，求bese的exponent次方
不得使用库函数，不需要考虑大数问题
'''

class Solution:
	'''
	注意：
	区分base是否为1
	区分exponent的正负情况
	'''
	def power(self, base, exponent):
		if base == 0:
			return 0
		else:
			if exponent == 0:
				return 1
			elif exponent > 0:
				for i in range(exponent-1):
					base *= base
				return base
			else:
				base = 1.0/base
				for i in range(-exponent-1):
					base *= base
				return base

if __name__ == '__main__':
	s = Solution()
	print s.power(2, 3), s.power(2,-2), s.power(5,0), s.power(0.0, -5)


