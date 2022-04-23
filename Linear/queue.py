class Queue:
    # A class to create a queue object. 
    # Uses a FIFO queuing policy
    def __init__(self):
        self.queue = []

    # Add an element at the end of the queue
    def enqueue(self, data):
        self.queue = [data] + self.queue

    # Remove an element in the front of the queue
    def dequeue(self):
        if len(self.queue) != 0:
            self.queue.pop()

    # Peek to the front of the queue
    def front():
        if len(self.queue) != 0:
            print(self.queue[-1])

    # Peek to the left of the queue
    def rear():
        if len(self.queue) != 0:
            print(self.queue[0])

    # Print out the queue 
    def print_queue(self):
        if len(self.queue) != 0:
            " -> ".join(self.queue)
