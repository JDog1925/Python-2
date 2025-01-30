class DequeQueue:
    def __init__(self):
        self.deque = [] #list to store the items

    def enqueue(self, item):
        self.deque.append(item)  # add an item to the queue

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.deque.pop(0) # remove item from front

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

deque_queue = DequeQueue()

deque_queue.enqueue(10)
deque_queue.enqueue(8)
deque_queue.enqueue(9)
deque_queue.enqueue(11)
print("Queue size after enqueues:",deque_queue.size())

#deque item
print("Dequeue items:", deque_queue.dequeue())
print("Dequeue items:", deque_queue.dequeue())
print("Dequeue items:", deque_queue.dequeue())

#Size
print("Queue size after dequeues:", deque_queue.size())

#empty queue
print("Queue empty?", deque_queue.is_empty())
