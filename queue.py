# Queue
# First-In-First-Out，FIFO

class Queue(object):
	def __init__(self):
		self.queue = []
		
	def enqueue(self, item):
		#在队列尾部加入一个数据项，参数是数据项，无返回值。
		self.queue.append(item)

	def dequeue(self):
		#删除队列头部的数据项，不需要参数，返回值是被删除的数据，队列本身有变化。
		if self.queue.is_empty():
			raise IndexError('Queue is empty!')
		self.queue.pop(0)
	
	def is_empty(self):
		#检测队列是否为空。无参数，返回布尔值。
		return len(self.queue) == 0
		
	def get_size(self):
		#返回队列数据项的数量。无参数，返回一个整数。
		return len(self.queue)


if __name__=='__main__':
	q=Queue()
	q.is_empty()
	print(q.get_size())
	q.enqueue(1)
	q.enqueue(2)
	print(q.get_size())
