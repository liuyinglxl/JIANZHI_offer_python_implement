# ----coding:utf-8--------
'''
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
'''

class Solution:
	'''
	自己的思路：遇到有序或者部分有序的查找，就用二分查找！
	二分查找的变体，只要找到前面一个值大于后面一个值，则后面这个就是最小值
	'''
	def rotating(self, array):
		array_len = len(array)
		low = 0
		high = array_len-1
		while low < high:
			mid = (low + high) / 2
			if array[mid]<=array[mid+1]:
				low = mid+1
			else:
				return array[mid+1]

if __name__ == '__main__':
	s = Solution()
	print s.rotating([3,4,5,1,2])