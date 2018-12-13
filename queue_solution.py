"""
Making a Queue class using a list.
Output will be returned with Python 2.7, but Python 3.0 will return
the following error message:

  File "queue_solution.py", line 40
    print q.peek()
          ^
SyntaxError: invalid syntax
"""


class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]
    """
    Insert. Here the argument i is the index of the element before which
    to insert the element x . Thus, a.insert(len(a), x) is the same thing
    as a.append(x) . ... If you only needed to add an element to the end
    of the list then append works just fine for that, and is faster (which
    matters for large lists).

    Start with checking if queue is empty first.
    """
    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]
    # Removing something from the queue.
    def dequeue(self):
        return self.storage.pop(0)
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()
