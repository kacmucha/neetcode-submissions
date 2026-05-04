class Node:

    def __init__(self, val=0, next=None):
        self.val = val;
        self.next = next;

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
        if self.guard.next:
            newNode.next = self.guard.next

        self.guard.next = newNode

        if self.tail == None:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.tail == None:
            self.guard.next = newNode
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        curr = self.guard
        for i in range(0, index):
            if curr.next:
                curr = curr.next
            else:
                return False
        
        if curr.next:
            if curr.next.next:
                curr.next = curr.next.next
            else:
                curr.next = None
                self.tail = curr
            return True
        return False

    def getValues(self) -> List[int]:
        resList = []
        curr = self.guard
        while curr.next:
            curr = curr.next
            resList.append(curr.val)
        
        return resList