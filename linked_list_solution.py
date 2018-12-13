"""
Solution works for Python 2.7, but not Python 3.0
The three functions added to LinkedList are get_position,
insert, and delete.
"""


class Element(object):
    def __init__(self, value):
        self.value = value
        # Storing pointer to the next node.
        self.next = None

# Wrapper that wraps over the above Element/Nodes.
class LinkedList(object):
    def __init__(self, head=None):
        # Want the head element/node available in the linked list. Will NOT
        # contain data and will NOT be indexable. Simply used as a placeholder
        # to allow us to point to the first element in the list.
        self.head = head

    # Creating first element of the list.
    def append(self, new_element):
        # Starting at left of the list.
        current = self.head
        if self.head:
            # Traverse through the list
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    # Returns an element at a certain position.
    # Extractor function.
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            # Traversing through the next node.
            current = current.next
            counter += 1
        return None

    # The insert function adds an element to a particular spot in the list.
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    # Deletes the first element with that particular value.
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
