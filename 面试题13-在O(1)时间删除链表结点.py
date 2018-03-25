# ------ coding: utf-8 ----------
'''
题目：给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点
'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	'''
	思路来自书上，已经get
	结点只有指向后面结点的指针，没有指向前面结点的指针
	按照传统解法，我们会从头结点开始，遍历结点，直到找到一个结点h，h的下一个结点是我们要删的结点，然后再来进行删除，
		这样的话，时间复杂度为O(n)
	按如果我们充分利用结点的指向后面的指针呢？要删的结点为i，下一个为j，再下一个为h；将j的值赋给i，将i指向h，
		则完成了删除结点i，时间复杂度为O(1)
	'''
	def deleteNode(self, head_node, del_node):
		if not head_node or not del_node:
			return
		# 只有一个结点，则删除改结点
		if head_node == del_node:
			head_node=del_node=None
		# 要删除的结点是尾结点，则需要顺序遍历
		elif del_node.next == None:
			while head_node:
				if head_node.next == del_node:
					head_node.next = None
				head_node = head_node.next
		# 其他普遍情况
		else:
			next_node = del_node.next
			del_node.val = next_node.val
			del_node.next = next_node.next
			next_node = None
		# 时间复杂度 ((n-1)*O(1)+O(n))/n = O(1)

if __name__ == '__main__':
	s = Solution()
	node1 = ListNode(10)
	node2 = ListNode(11)
	node3 = ListNode(13)
	node4 = ListNode(15)
	node1.next = node2
	node2.next = node3
	node3.next = node4

	print(node3.val)
	s.deleteNode(node1, node3)
	print(node3.val)

