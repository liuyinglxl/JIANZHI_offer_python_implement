# -----coding:utf-8-------
'''
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
import os

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	'''
	我的思路：前序的第一个为根结点，在中序中找到该位置，左边的为左节点部分，右边的为右节点部分
	然后遍历
	'''
	def rebuild(self, pre_list, mid_list):
		if not pre_list or not mid_list:
			return None
		root = TreeNode(pre_list[0])
		idx = mid_list.index(pre_list[0])

		root.left = self.rebuild(pre_list[1:(idx+1)], mid_list[:idx])
		root.right = self.rebuild(pre_list[(idx+1):], mid_list[(idx+1):])
		return root


if __name__ == '__main__':
	s = Solution()
	p = s.rebuild([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
	while p != None:
		print p.val
		p = p.left







