# ------- coding:utf-8 --------
'''
题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reverseList(self, head_node):
		prev_node  = None
		current_node = head_node
		next_node = None
		reverse_head_node = None

		while current_node != None:
			next_node = current_node.next
			if next_node == None:
				reverse_head_node = current_node
			current_node.next = prev_node

			prev_node = current_node
			current_node = next_node
		return reverse_head_node

if __name__ == '__main__':
	s = Solution()
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	d = ListNode(4)
	e = ListNode(5)
	a.next = b
	b.next = c
	c.next = d
	d.next = e

	head = s.reverseList(a)
	print head.val
	head = head.next
	print head.val
	head = head.next
	print head.val
	head = head.next
	print head.val
	head = head.next
	print head.val





		






