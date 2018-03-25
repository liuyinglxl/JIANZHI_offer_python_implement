# ---coding:utf-8-------
'''
题目：输入一个链表，从尾到头打印链表每个节点的值。
'''
import os

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
	def print_link(self, listNode):
		result = []
		while listNode.next is not None:
			result.append(listNode.val)
			listNode = listNode.next
		result.append(listNode.val)
		result.reverse()
		return result

if __name__ == '__main__':
	s = Solution()
	# 初始化链表
	p = head = ListNode(-1)
	for i in range(5):
		p.next = ListNode(i)
		p = p.next
	print s.print_link(head)








