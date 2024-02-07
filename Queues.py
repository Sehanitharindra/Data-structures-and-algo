#create a class for queue
class Queue:
    def __init__(self, size):
        #properties of queue
        self.size = size
        self.queue = [None] * size
        self.head = 0
        self.tail = 0

    #enqueue elements to queue
    def enqueue(self, x):
        self.queue[self.tail] = x
        if self.tail == self.head:
            self.tail = 1
        else:
            self.tail = self.tail + 1

    #dequeue elements from queue
    def dequeue(self):
        x = self.queue[self.head]
        if self.tail == self.head:
            self.head = 1
        else:
            self.head = self.head + 1
        return x

#example use of queue and it operations
queue_size = 5
my_queue = Queue(queue_size)


my_queue.enqueue(10) # add 10
my_queue.enqueue(20) # add 20
my_queue.enqueue(30) # add 30
my_queue.enqueue(50) # add 50


print("Dequeued element:", my_queue.dequeue())  # print 10
print("Dequeued element:", my_queue.dequeue())  # print 20
print("Dequeued element:", my_queue.dequeue())  # print 30

