class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Add to head
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Delete by value
    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
    
    # Update by index
    def update(self, index, new_data):
        current = self.head
        for _ in range(index):
            if not current:
                return
            current = current.next
        if current:
            current.data = new_data
    
    # Search
    def search(self, target):
        current = self.head
        idx = 0
        while current:
            if current.data == target:
                return idx
            current = current.next
            idx += 1
        return -1

