class Node(object):
    """单链表的结点"""
    def __init__(self,item):        
        self.item = item                   #item存放数据元素        
        self.next = None                   #next是下一个节点的标识


class singleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None
 
    def is_empty(self):
        return self._head == None
 
    def get_length(self):        
        current = self._head                   #current初始时指向头节点
        count = 0
        while current != None:                 #尾节点指向None，当未到达尾部时
            count += 1
            current = current.next                 #将current后移一个节点
        return count
 
    def travel(self):
        current = self._head
        while current != None:
            print(current.item)
            current = current.next
        print('')

    def append(self, item):
        node = Node(item)

        if self.is_empty():
            self._head = node
        else:
            current = self._head
            while current.next!=None:
                current = current.next
            current.next = node
    
    def add(self, item):	    
	    node = Node(item)                   #先创建一个保存item值的节点
	    node.next = self._head              #将新节点的链接域next指向头节点，即_head指向的位置
	    self._head = node                   #将链表的头_head指向新节点

    def remove(self,item):
        current = self._head
        prev = None
        while current != None:                          
            if current.item == item:        #找到了指定元素                
                if not prev:                #如果第一个就是删除的节点                    
                    self._head = current.next #将头指针指向头节点的后一个节点
                else:
                    prev.next = current.next #将删除位置前一个节点的next指向删除位置的后一个节点
                break
            else:
                prev = current               #继续按链表后移节点
                current = current.next

 
 
class cycleLinkedlist(object):
    """单向循环链表"""
    def __init__(self):
        self._head = None
 
    def is_empty(self):
        return self._head == None
 
    def get_length(self):
        if self.is_empty():
            return 0
        count = 1
        current = self._head
        while current.next != self._head:  #主要区别
            count += 1
            current = current.next
        return count
 
    def travel(self):
        if self.is_empty():
            return
        current = self._head
        print(current.item)
        while current.next != self._head:
            current = current.next
            print(current.item)
        print("")
 
 
    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            node.next = self._head
            current = self._head
            while current.next != self._head:
                current = current.next
            current.next = node
            #_head指向添加node的
            self._head = node
 
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            current = self._head
            while current.next != self._head:
                current = current.next
            current.next = node
            node.next = self._head   #主要区别
 
    def insert(self, position, item):
        if position <= 0:
            self.add(item)
        elif position > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            current = self._head
            count = 0
            while count < (position-1):
                count += 1
                current = current.next
            node.next = current.next
            current.next = node
 
    def remove(self, item):
        if self.is_empty():
            return
        current = self._head
        pre = None
        if current.item == item:
            if current.next != self._head:
                while current.next != self._head:
                    current = current.next
                current.next = self._head.next
                self._head = self._head.next
            else:
                self._head = None
        else:
            pre = self._head
            while current.next != self._head:
                if current.item == item:
                    pre.next = current.next
                    return
                else:
                    pre = current
                    current = current.next
            if current.item == item:
                pre.next = current.next

 
if __name__ == "__main__":
    ll1 = cycleLinkedlist()
    ll1.add(1)
    ll1.add(2)
    ll1.append(3)
    print("length:",ll1.get_length())
    ll1.remove(1)
    print("length:",ll1.get_length())
    ll1.travel()
