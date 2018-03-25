# ------ coding:utf-8 --------
'''
题目：请完成一个函数，输出一个二叉树，该函数输出它的镜像
其实就是对称、翻转的意思，像照镜子一样的结果
'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	'''
	书上的解法：镜像，画个图就能看出来，其实交换所有结点的左右子结点即可
	利用递归
	'''
	def mirror(self, root_node):
		if root_node == None:
			return
		tmp = root_node.left
		root_node.left = root_node.right
		root_node.right = tmp

		self.mirror(root_node.left)
		self.mirror(root_node.right)


if __name__ == '__main__':
	s = Solution()
	a = TreeNode(8)
	b1 = TreeNode(6)
	b2 = TreeNode(10)
	c1 = TreeNode(5)
	c2 = TreeNode(7)
	c3 = TreeNode(9)
	c4 = TreeNode(11)
	a.left = b1
	a.right = b2
	b1.left = c1
	b1.right = c2
	b2.left = c3
	b2.right = c4

	s.mirror(a)
	root = a
	print root.val, root.left.val, root.right.val
	root1 = root.left
	print root1.val, root1.left.val, root1.right.val
	root2 = root.right
	print root2.val, root2.left.val, root2.right.val

