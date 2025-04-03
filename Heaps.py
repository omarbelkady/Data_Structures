class Heap:
    def __init__(self):
        self.heap=[]
        self.size=0
    def parent(self,i):
        return((i-1)//2)
    def right_child(self, i):
        return((2*i)+2)
    def left_child(self, i):
        return((2*i)+1)
    def find_min(self):
        if(self.size<=0):
            return None
        else:
            return self.heap[0]
    def swap(self,i,j):
        self.heap[i],self.head[j]=self.heap[j],self.heap[i]
    def heapify_up(self, i):
        parent_index=self.heap(i)
        if(i<=0 or self.heap[parent_index] < self.heap[i]):
            return
        self.swap(i, parent_index)
        self.heapify_up(parent_index)
    def heapify_down(self,i):
        smallest=i
        left=self.left_child(i)
        right=self.right_child(i)

        if(left < self.size and self.heap[left]<self.heap[smallest]):
            smallest=left
        if(right<self.size and self.heap[right]<self.heap[smallest]):
            smallest=right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)

    def insert(self, key):
        self.heap.append(key)
        self.size+=1
        self.heapify_up(self.size-1)
    
    def extract_min(self):
        if self.size<=0:
            return None
        min_val=self.heap[0]

        self.heap[0]=self.heap[self.size-1]
        self.size -= 1
        self.heap.pop()

        self.heapify_down(0)

        return min_val
    
    def reduce_key(self, i, new_value):
        if i >= self.size or new_value > self.heap[i]:
            return False
        self.heap[i]=new_value
        self.heapify_up(i)
        return True
    
    def delete_key(self, i):
        if i >= self.size:
            return False
        self.delete_key(i,float('-inf'))
        self.extract_min()
        return True
    
    def __str__(self):
        return str(self.heap[:self.size])


