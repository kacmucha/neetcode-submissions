class Node:

    def __init__(self, val=0, next=None):
        self.val = val;
        self.next = next;
        self.hasNext = False

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.guard = Node(None, None)

    def get(self, index: int) -> int:
        curr = self.guard.next

        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.guard.hasNext:
            newNode.next = self.guard.next
            newNode.hasNext = True

        self.guard.next = newNode
        self.guard.hasNext = True

        if self.tail == None:
            self.tail = newNode
            

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.tail == None:
            self.guard.next = newNode
            self.guard.hasNext = True
            self.head = newNode
            self.tail = newNode
            return

        self.tail.hasNext = True
        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        self.head = self.guard
        for i in range(0, index):
            if self.head.hasNext == False:
                return False
            self.head = self.head.next
        
        if self.head.hasNext:
            if self.head.next.hasNext:
                self.head.next = self.head.next.next
            else:
                self.head.next = None
                self.head.hasNext = False
                self.tail = self.head
            return True
        return False

    def getValues(self) -> List[int]:
        resList = []
        self.head = self.guard
        while self.head.hasNext:
            self.head = self.head.next
            resList.append(self.head.val)
        
        return resList