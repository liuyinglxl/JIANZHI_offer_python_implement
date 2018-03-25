# -----coding: utf-8------
'''
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
网上的思路：
A用来入栈，B用来出栈
入栈：直接进入A
出栈：如果B中有元素，则将B中最上面一个pop；如果B中没有元素，则将A中的元素全部依次出栈压入B中，再对B进行pop
'''
class Solution:
	def __init__(self):
		self.stackA = []
		self.stackB = []

	def pop(self):
		# B中有元素
		if self.stackB:
			return self.stackB.pop()
		# B中没有元素，而且A中也没有元素
		elif not self.stackA:
			return None
		# B中没有元素，但是A中有元素
		else:
			while self.stackA:
				self.stackB.append(self.stackA.pop())
			return self.stackB.pop()

	def push(self, node):
		self.stackA.append(node)

if __name__ == '__main__':
	s = Solution()
	s.stackA = [1,2,3,4,5]
	print s.pop()
	s.push(8)
	while s.stackA:
		print s.pop()

