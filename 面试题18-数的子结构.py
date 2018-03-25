# ------ coding:utf-8 ----------
'''
题目：输入两颗二叉树A和B，判断B是不是A的子结构
'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	'''
	书上的思路：遍历father，如果father的根结点和child的根结点一样的话，就调用doesTree1haveTree2判断接下来的结构是否一样
	如果father的根结点不与child的根结点一样的时候，就遍历father
	'''
	def hasSubTree(self, father_root_node, child_root_node):
		result = False
		if father_root_node != None and child_root_node != None:
			if father_root_node.val == child_root_node.val:
				result = self.doesTree1haveTree2(father_root_node, child_root_node)
			if not result:
				result = self.hasSubTree(father_root_node.left, child_root_node)
			if not result:
				result = self.hasSubTree(father_root_node.right, child_root_node)
		return result

	def doesTree1haveTree2(self, father_root_node, child_root_node):
		# 这里一定要先判断child是否为空，再判断father
		if child_root_node == None:
			return True
		if father_root_node == None:
			return False
		if father_root_node.val != child_root_node.val:
			return False
		return self.doesTree1haveTree2(father_root_node.left, child_root_node.left) and \
			self.doesTree1haveTree2(father_root_node.right, child_root_node.right)


if __name__ == '__main__':
	s = Solution()
	a = TreeNode(8)
	b1 = TreeNode(8)
	b2 = TreeNode(7)
	c1 = TreeNode(9)
	c2 = TreeNode(2)
	d1 = TreeNode(4)
	d2 = TreeNode(7)
	a.left = b1
	a.right = b2
	b1.left = c1
	b1.right = c2
	c2.left = d1
	c2.right = d2

	p = TreeNode(8)
	p.left = TreeNode(9)
	p.right = TreeNode(2)

	print s.hasSubTree(a, p)




