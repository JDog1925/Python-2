class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) # add an item to the queue

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

queue = queue()

queue.enqueue(7)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.dequeue()#no argument passed here
print("Dequeue item: ", queue.dequeue())
print("Size of the queue is: ", queue.size())

print("Is the queue empty? ", queue.is_empty())