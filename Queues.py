
def enqueue(queue, element):
    queue.append(element)
    return queue

def dequeue(queue):
    if queue:
        return queue.pop(0)
    return None

def front(queue):
    return queue[0] if queue else None

# Example Usage:
queue = []
enqueue(queue, "A")  # ["A"]
enqueue(queue, "B")  # ["A", "B"]
dequeue(queue)       # Returns "A" → queue ["B"]