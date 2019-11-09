from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList

class SortedListPQ(PriorityQueueBase): # base class defines _Item
  """A min-oriented priority queue implemented with an unsorted list."""

  def __init__(self):
    """Create a new empty Priority Queue."""
    self._data = PositionalList()

  def __len__(self):
    """Return the number of items in the priority queue."""
    return len(self._data)

  def add(self, key, value):
    """Add a key-value pair."""
    newest = self._Item(key, value)
    walk = self._data.last()
    while walk is not None and newest < walk.element():
        walk = self._data.before(walk)
    if walk is None:
        self._data.add_first(newest)
    else:
        self._data.add_after(walk, newest)

  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.
    Raise Empty exception if empty.
    """
    if self.is_empty():
        raise Empty("Priority queue is empty")
    p = self._data.first()
    item = p.element()
    return item._key, item._value

  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.
    Raise Empty exception if empty.
    """
    if self.is_empty():
        raise Empty("Priority queue is empty")
    item = self._data.delete(self._data.first())
    return (item._key, item._value)

if __name__ == '__main__':
    P = SortedListPQ()

    ## Uncomment this section to allow user to input into the program

    '''ans = " "
    count = 0
    K = {}
    V = {}
    while ans != "N" and ans != "n":
        key = int(input("What is the key of your entry?"))
        value = int(input("What is the value of your entry?"))
        K[count] = key
        V[count] = value
        ans = input("Continue entering values? (Y/N)")
        count += 1
    '''
    K = [7, 4, 8, 2, 5, 3, 9]
    V = [10, 58, 16, 23, 41, 85, 2]

    print("List before being added to the Priority Queue:")
    for i in range(len(K)):  # prints the sequence before being added to the PQ
        print("(" + str(K[i]) + ", " + str(V[i]) + ")")

    # uses the 2 arrays holding the keys and values to insert them into the PQ
    for i in range(len(K)):
        P.add(K[i], V[i])
    # prints the sequence after being added and removed from the PQ
    print("List after being added to the Priority Queue: ")
    for i in range(len(K)):
        print(P.remove_min())
