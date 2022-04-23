class Stack:
    # A class to create a stack object. 
    # Uses a LIFO queuing policy
    def __init__(self):
        self.stack = []

    # Add an element at the end of the queue
    def push(self, data):
        self.stack.append(data)

    # Remove an element in the front of the queue
    def pop(self):
        if len(self.stack) != 0:
            self.queue.pop()

    # Peek to the top of the stack
    def peek():
        if len(self.stack) != 0:
            print(self.stack[-1])

    # Print out the queue 
    def print_queue(self):
        if len(self.stack) != 0:
            " -> ".join(self.stack)
