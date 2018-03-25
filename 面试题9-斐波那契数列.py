# ----coding:utf-8-------
'''
写一个函数，输入n，求斐波那契数列的第n项
斐波那契数：
f(0)=0
f(1)=1
f(n)=f(n-1)+f(n-2) (n>=2)
'''

class Solution:
	'''
	自己的解法：从n到0依次迭代，但是存在一个问题，很多数背重复计算，时间复杂度太高
	'''
	def fibonacci(self, n):
		if n == 0 or n == 1:
			return n
		else:
			return self.fibonacci(n-1) + self.fibonacci(n-2)

	'''
	改进算法：从0到n迭代，每次都通过前面两个数来计算，不会重复计算，大大减少时间复杂度
	'''
	def fibonacci2(self, n):
		result = [0, 1]
		for i in range(2, n+1):
			result.append(result[i-1] + result[i-2])
		return result[n]

if __name__ == '__main__':
	s = Solution()
	print s.fibonacci(5), s.fibonacci(10), s.fibonacci(15)
	print s.fibonacci2(5), s.fibonacci2(10), s.fibonacci2(15)



