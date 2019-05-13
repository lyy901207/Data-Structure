#用数组实现一个顺序栈

class Stack(object):
	
	def __init__(self):
		self.items = []

	def push(self, item): 
		#向栈顶插入项
		self.items.append(item)

	def pop(self):
		#返回栈顶的项，并从堆栈中删除该项
		self.items.pop()

	def clear(self):
		#清空堆栈
		del self.items[:]

	def is_empty(self):
		#判断堆栈是否为空
		return len(self.items) == 0

	def get_size(self): 
		#返回堆栈中项的个数
		return len(self.items)

	def top(self): 
		#返回栈顶的项
		return self.items[-1]

if __name__ =='__main__':
	s = Stack()
	print(s.is_empty())
	s.push(1)
	s.push(2)
	s.is_empty()
	print(s.get_size())
	s.get_size()
	s.top()
	s.pop()
	s.clear()
	s.is_empty()
	print(s.get_size())