# cycle queue

class CycleQueue(object):

	def __init__(self, capability):
		self.queue = [None] * capability
		self.capability = capability
		self.front = 0
		self.rear = 0

	
	def get_length(self):
		# 返回当前队列的长度
		return (self.rear - self.front + self.capability) % self.capability 

	
	def enqueue(self, val):
		# 如果队列未满，则在队尾插入元素
		if (self.rear + 1) % self.capability == self.front:          #%取余可以实现循环
			raise IndexError("The queue is full!")
		else:
			self.queue[self.rear] = val
			self.rear = (self.rear + 1) % self.capability

	def dequeue(self):
		if self.rear == self.front:
			raise IndexError("The queue is empty!")
		else:
			item = self.queue[self.front]
			self.queue[self.front] = None
			self.front = (self.front + 1) % self.capability
			return item

	# 输出队列中的元素
	def travel(self):
		for i in range(self.capability):
			print(self.queue[i],end=',')
		print(' ')


if __name__ == "__main__":
    q = CycleQueue(10)
    for i in range(5):
        q.enqueue(i)
    q.travel()
    # 删除队头的5个元素：0~4
    for i in range(2):
        q.dequeue()
    q.travel()
    # 从队尾增加8个元素：0~7
    for i in range(2):
        q.enqueue(i)
    q.travel()
