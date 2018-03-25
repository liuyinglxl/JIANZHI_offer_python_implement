# ----- coding:utf-8 ---------
'''
题目：输入一个链表，输出该链表中倒数第k个结点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第1个结点。
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	'''
	自己的思路：遍历两次链表，第一次记录链表的长度
	'''
	def findKthTail(self, head_node, k):
		if not head_node:
			return
		length = 0
		tmp_node = head_node
		while tmp_node:
			length += 1
			tmp_node = tmp_node.next
		if k > length:
			print "k is bigger than list length"
			return
		else:
			index = length-k
			i = 0
			while i < index:
				head_node = head_node.next
				i += 1
			return head_node

	'''
	方法来自书上：只用遍历一次链表
	只用遍历一次链表，找到倒数第k个，用两个指针front，last
	首先先用front遍历前k-1个，然后同时移动front和last，直到front到达尾结点，此时last指向的就是要找的结点
	注意边界情况
	'''
	def findKthTail2(self, head_node, k):
		if k <= 0 or head_node == None:
			print "k is wrong!"
			return
		else:
			front_node = head_node
			last_node = head_node
			for i in range(0, k-1):
				front_node = front_node.next
			while front_node.next:
				front_node = front_node.next
				last_node = last_node.next
			return last_node



if __name__ == '__main__':
	s = Solution()
	a1 = ListNode(1)
	a2 = ListNode(2)
	a3 = ListNode(3)
	a4 = ListNode(4)
	a5 = ListNode(5)
	a6 = ListNode(6)

	a1.next = a2
	a2.next = a3
	a3.next = a4
	a4.next = a5
	a5.next = a6

	# node1 = s.findKthTail(a1, 3)
	node2 = s.findKthTail2(a1, 3)
	# print node1.val
	print node2.val
	node = s.findKthTail(a1, 10)





