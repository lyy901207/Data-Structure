#lnked list queue# linked list stack

class Node(object):
	def __init__(self, item = None):
		self.item = item
		self.next = None

class LinkedListQueue(object):
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
			temp = self.top
			while temp.next:
				temp = temp.next
			temp.next = cur      
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
			raise IndexError("Queue is empty!")
		else:
			cur = self.top
			while self.count > 0 and cur:
				print(cur.item)
				cur = cur.next




if __name__ == '__main__':
    llq = LinkedListQueue()
    for i in range(1, 5):
        llq.push(i)
    llq.travel()
    llq.pop()
    llq.travel()