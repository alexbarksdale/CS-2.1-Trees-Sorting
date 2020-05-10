#!python

from binaryheap import BinaryMinHeap


class PriorityQueue(object):
    """PriorityQueue: a partially ordered queue with methods to enqueue items
    in priority order and to access and dequeue its highest priority item.
    Item pairs are stored in a binary min heap for its efficient operations."""

    def __init__(self):
        """Initialize this priority queue."""
        # Initialize new binary min heap to store items in this priority queue
        self.heap = BinaryMinHeap()

    def __repr__(self):
        """Return a string representation of this priority queue."""
        return 'PriorityQueue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this priority queue is empty, or False otherwise."""
        return self.heap.is_empty()

    def length(self):
        """Return the number of items in this priority queue."""
        return self.heap.size()

    def enqueue(self, item, priority):
        """Insert the given item into this priority queue in order according to
        the given priority."""
        # New item to enqueue
        new_item = (priority, item)
        # Insert given item into heap in order according to given priority
        self.heap.insert(new_item)

    def front(self):
        """Return the item at the front of this priority queue without removing
        it, or None if this priority queue is empty."""
        if self.heap.size() == 0:
            return None
        # Return minimum item from heap
        return self.heap.get_min()

    def dequeue(self):
        """Remove and return the item at the front of this priority queue,
        or raise ValueError if this priority queue is empty."""
        if self.heap.size() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # Remove and return minimum item from heap
        self.heap.delete_min()

    def push_pop(self, item, priority):
        """Remove and return the item at the front of this priority queue,
        and insert the given item in order according to the given priority.
        This method is more efficient than calling dequeue and then enqueue."""
        if self.heap.size() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # New item to replace
        replaced_item = (priority, item)
        # Replace and return minimum item from heap
        self.heap.replace_min(replaced_item)


if __name__ == "__main__":
    T1 = [('Hulk', 8), ('Deadpool', 1), ('Thor', 2), ('Bob the Builder', 3)]

    q = PriorityQueue()
    for item in T1:
        # Unpack values from item (tuple)
        item_val, priority = item
        q.enqueue(item_val, priority)

    print(f'First person in queue: {q}')
    q.push_pop('Ironman', 0)
    print('\nThe previous first person has been removed!')
    print(f'Big man arrived and moved up to the front {q}')
    q.dequeue()
    print(f'\nDequeued Iron Man, expecting Thor: {q}')
    q.enqueue('Timmy Turner', 0)
    print(f'\nEntering Timmy Turner to the front: {q}')
