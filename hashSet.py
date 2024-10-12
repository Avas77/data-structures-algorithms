class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self) -> None:
        self.head = None

    def add(self, key):
        if not self.contains(key):
            node = Node(key)
            node.next = self.head
            self.head = node
        return self.head

    def contains(self, key):
        node = self.head 
        while node:
            if node.val == key:
                return True
            node = node.next
        return False
    
    def getNode(self):
        return self.head
        

buddy = MyHashSet()
buddy.add(2)
buddy.add(3)
print(buddy.getNode().next.val)