class PriorityQueue:
    def __init__(self):
        """Initialize an empty priority queue using a min heap"""
        self.heap = []
    
    def __len__(self):
        """Return the number of elements in the queue"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if the priority queue is empty"""
        return len(self.heap) == 0
    
    def _parent(self, idx):
        """Return the parent index of the element at idx"""
        return (idx - 1) // 2
    
    def _left_child(self, idx):
        """Return the left child index of the element at idx"""
        return 2 * idx + 1
    
    def _right_child(self, idx):
        """Return the right child index of the element at idx"""
        return 2 * idx + 2
    
    def _swap(self, i, j):
        """Swap elements at indices i and j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _sift_up(self, idx):
        """Move element up to maintain heap property"""
        parent = self._parent(idx)
        # If element has higher priority (lower value) than parent, swap
        if idx > 0 and self.heap[parent][0] > self.heap[idx][0]:
            self._swap(idx, parent)
            # Continue sifting up
            self._sift_up(parent)
    
    def _sift_down(self, idx):
        """Move element down to maintain heap property"""
        smallest = idx
        left = self._left_child(idx)
        right = self._right_child(idx)
        
        # Find smallest among node and its children
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
            
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
            
        # If one of the children is smaller, swap and continue sifting down
        if smallest != idx:
            self._swap(idx, smallest)
            self._sift_down(smallest)
    
    def enqueue(self, priority, item):
        """Add an item with the given priority to the queue"""
        # Lower priority value means higher priority
        self.heap.append((priority, item))
        # Fix heap property by moving element up as needed
        self._sift_up(len(self.heap) - 1)
    
    def dequeue(self):
        """Remove and return the highest priority item"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
            
        # The root has the highest priority
        priority, item = self.heap[0]
        
        # Move last element to root and remove last element
        if len(self.heap) > 1:
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            # Fix heap property by moving element down as needed
            self._sift_down(0)
        else:
            self.heap.pop()
            
        return item
    
    def peek(self):
        """Return the highest priority item without removing it"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.heap[0][1]
    
    def update_priority(self, item, new_priority):
        """Update the priority of an item (find by equality)"""
        # Linear search for the item (not efficient for large queues)
        for i in range(len(self.heap)):
            if self.heap[i][1] == item:
                old_priority = self.heap[i][0]
                self.heap[i] = (new_priority, item)
                
                # Depending on whether priority increased or decreased
                if new_priority < old_priority:
                    self._sift_up(i)
                else:
                    self._sift_down(i)
                return True
        return False
    
    def __str__(self):
        """String representation of the priority queue"""
        return str([(p, str(i)) for p, i in self.heap])

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    
    # Enqueue tasks with priorities (lower number = higher priority)
    pq.enqueue(3, "Check email")
    pq.enqueue(1, "Emergency task")
    pq.enqueue(2, "Prepare presentation")
    pq.enqueue(5, "Regular task")
    
    print("Priority Queue:", pq)
    
    # Process highest priority tasks first
    print("Processing:", pq.dequeue())  # Should be "Emergency task"
    print("Processing:", pq.dequeue())  # Should be "Prepare presentation"
    
    # Update priority of an existing task
    pq.update_priority("Regular task", 0)  # Make it highest priority
    print("Priority Queue after update:", pq)
    
    print("Next task to process:", pq.peek())