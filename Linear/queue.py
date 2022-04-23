class Queue:
    # A class to create a queue object. 
    # Uses a FIFO policy
    def __init__(self):
        self.queue = []

    # Add an element at the end of the queue
    def enqueue(self, data):
        self.queue = [data] + self.queue

    # Remove an element in the front of the queue
    def dequeue(self):
        self.queue.pop()

    # Print out the queue 
    def print_queue(self):
        " -> ".join(self.queue)
