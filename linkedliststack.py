# linked list stack

class Node(object):
	def __init__(self, item = None):
		self.item = item
		self.next = None

class LinkedListStack(object):
	def __init__(self):
		self.top = Node()
		self.count = 0

	def get_size(self):
		return self.count

	def is_empty(self):
		return self.count==0

	def push(self, val):
		cur = Node(val)
		if self.is_empty():
			self.top = cur
		else:
			cur.next = self.top      # 原来的栈顶变成了cur的next， 再将栈顶设为cur
			self.top = cur
		self.count += 1

	def pop(self):
		if self.is_empty():
			raise IndexError('The stack is empty!')
		else:
			pop_value = self.top.item
			self.top = self.top.next
			self.count -= 1
			return pop_value

	
	def travel(self):
		if self.is_empty():
			raise IndexError("Stack is empty!")
		else:
			cur = self.top
			while self.count > 0 and cur:
				print(cur.item)
				cur = cur.next




if __name__ == '__main__':
    lls = LinkedListStack()
    for i in range(1, 5):
        lls.push(i)
    lls.travel()
    lls.pop()
    lls.travel()