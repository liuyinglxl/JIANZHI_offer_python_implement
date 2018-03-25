# -------- coding:utf-8 ----------
'''
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是递增排序的
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	'''
	本题最开始自己的思路，是逐个比较，不用递归，但是需要考虑的特殊情况太多，所以利用书上的递归来做。
	递归实现！
	'''
	def mergeList(self, a_head_node, b_head_node):
		if a_head_node == None:
			return b_head_node
		if b_head_node == None:
			return a_head_node

		merge_head = None
		if a_head_node.val < b_head_node.val:
			merge_head = a_head_node
			merge_head.next = self.mergeList(a_head_node.next, b_head_node)
		else:
			merge_head = b_head_node
			merge_head.next = self.mergeList(a_head_node, b_head_node.next)
		return merge_head

if __name__ == '__main__':
	s = Solution()
	a1 = ListNode(1)
	a2 = ListNode(3)
	a3 = ListNode(5)
	a1.next = a2
	a2.next = a3

	b1 = ListNode(2)
	b2 = ListNode(4)
	b3 = ListNode(6)
	b1.next = b2
	b2.next = b3

	head = s.mergeList(a1, None)
	while head != None:
		print head.val
		head = head.next










