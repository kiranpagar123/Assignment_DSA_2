class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
        
    def enqueue(self, element):
        self.enqueue_stack.append(element)
        
    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            raise IndexError("Queue is empty")
        return self.dequeue_stack.pop()
        
    def peek(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            raise IndexError("Queue is empty")
        return self.dequeue_stack[-1]
        
    def isEmpty(self):
        return not self.enqueue_stack and not self.dequeue_stack
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # output: 1
print(q.peek())     # output: 2
print(q.isEmpty())  # output: False
q.dequeue()
q.dequeue()
print(q.isEmpty())  # output: True
