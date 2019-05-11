# 双向链表实现

class Node(object):
    '''
    定义节点
    '''
    def __init__(self, item):
        self.item = item  #节点值
        self.next = None  #下一个节点的指针
        self.prev = None  #前一个节点的指针

  
class doubleLinkList(object):
    """双向链表"""
    def __init__(self):
        self._head = None
 
    def is_empty(self):
        '''判断链表是否为空'''
        return self._head == None
 
    def get_length(self):
        '''遍历操作与单链表一致'''
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
 
    def travel(self):
        '''遍历操作与单链表一致'''
        current = self._head
        while current != None:
            print(current.item)
            current = current.next
        print("")
    

    def add(self, item):
        '''头部插入元素'''
        node = Node(item)
        if self.is_empty():
            self._head = node           #如果是空链表，将_head指向node
        else:            
            node.next = self._head      #将node的next指向_head的头节点            
            self._head.prev = node      #将_head的头节点的prev指向node
            self._head = node           #将_head 指向node


    def append(self, item):
        '''尾部插入元素'''
        node = Node(item)
        if self.is_empty():            
            self._head = node           #如果是空链表，将_head指向node
        else:
            current = self._head            #移动到链表尾部
            while current.next != None:
                current = current.next
            current.next = node             #将尾节点cur的next指向node      
            node.prev = current             #将node的prev指向cur

    def insert(self, position, item):
        '''在指定位置添加节点'''
        if position <= 0:              #在头部插入 
            self.add(item)
        elif position > (self.get_length()-1):
            self.append(item)          #在尾部插入
        else:
            node = Node(item)          #移动到指定位置的前一个位置
            current = self._head
            count = 0
            while count < (position-1):
                count += 1
                current = current.next              
            node.prev = current            #将node的prev指向cur            
            node.next = current.next       #将node的next指向cur的下一个节点    
            current.next.prev = node       #将cur的下一个节点的prev指向node
            current.next = node            #将cur的next指向node

    def remove(self, item):
        '''删除元素'''
        if self.is_empty():
            return
        else:
            current = self._head
            if current.item == item:          #如果首节点的元素即是要删除的元素
                if current.next == None:
                    self._head = None     #如果链表只有这一个节点
                else:                   
                    current.next.prev = None  #将第二个节点的prev设置为None
                    self._head = current.next #将_head指向第二个节点
                return
            while current != None:
                if current.item == item:      #将cur的前一个节点的next指向cur的后一个节点
                    current.prev.next = current.next  #将cur的后一个节点的prev指向cur的前一个节点
                    current.next.prev = current.prev
                    break
                current = current.next


if __name__ == "__main__":
    ll = doubleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:",ll.get_length())
    ll.travel()
    ll.remove(1)
    print("length:",ll.get_length())
    ll.travel()