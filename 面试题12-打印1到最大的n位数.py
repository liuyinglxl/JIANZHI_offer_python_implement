# -------- coding: utf-8 ---------
'''
题目：输入数字n，按顺序打印出从1到最大的n位十进制数。
比如输入3，则打印1、2、3一直到最大的3位数即999.
'''

'''
本题的解法来自网上
本题是一个大数问题，将数字变成字符串来处理，需要实现在字符串上面的模拟加法
'''

class Solution:
	def print1ToMax(self, num):
		if num <= 0:
			return
		number = ['0']*num
		for i in range(10):
			number[0] = str(i)
			self.print1ToMaxRecursive(number, num, 0)


	def print1ToMaxRecursive(self, number, length, index):
		if index == length - 1:
			self.printNumber(number)
			return
		for i in range(10):
			number[index+1] = str(i)
			self.print1ToMaxRecursive(number, length, index+1)

	def printNumber(self, number):
		isBeginning0 = True 
		nLength = len(number)

		tmp_str = ""
		for i in range(nLength):
			if isBeginning0 and number[i] != '0':
				isBeginning0 = False
			if not isBeginning0:
				tmp_str += number[i]
		if tmp_str and tmp_str != None:
			print tmp_str
		

if __name__ == '__main__':
	s = Solution()
	if s.print1ToMax(3):
		print s.print1ToMax(3)





