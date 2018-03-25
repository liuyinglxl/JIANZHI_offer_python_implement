# ------coding:utf-8------------
'''
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution(object):
	'''
	自己的解法：将string转成list，找到空格替换成指定字符，再转回string
	'''
	def replace(self, string):
		str_list = list(string)
		for i in range(len(str_list)):
			if str_list[i] == ' ':
				str_list[i] = '%20'
		return "".join(str_list)

	'''
	利用str中的函数 replace
	'''
	def replace2(self, string):
		return string.replace(' ', '%20')

if __name__ == '__main__':
	s = Solution()
	print s.replace("We are happy.")
	print s.replace2("We are happy.")
			

