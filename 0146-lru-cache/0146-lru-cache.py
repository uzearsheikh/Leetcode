class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev= None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}      #isme hame key--> node rakhenge
        self.head = Node(0, 0)   # Dummy head: LRU side ki boundary
        self.tail = Node(0, 0)   # Dummy tail: MRU side ki boundary
        # head ⇄ tail , head and tail are two dummy nodes 
        self.head.next = self.tail
        self.tail.prev = self.head
        # Linked List: head ⇄ LRU ⇄ ... ⇄ MRU ⇄ tail


# Step 3 = add() function. Iska kaam hai kisi node ko tail ke just pehle insert karna, yani usko MRU banana.
    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
    # head → node → tail
        self.tail.prev.next = node
        self.tail.prev = node


# BEFORE:
# A ⇄ tail

# NEW NODE :: N

# AFTER:
# A ⇄ N ⇄ tail
    def remove(self, node):
        node.prev.next = node.next   # Previous node ko next node se connect
        node.next.prev = node.prev   # Next node ko previous node se connect
# N.prev.next = N.next
# N.next.prev = N.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]   #key --> node
        # ab node ko  use kra na apan ne to wo mru hogaya most recetly used towaha se hatao or next mru ki jagah krdo
        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # CASE 1 : IF THE KEY ALREADY EXIST THEN UPDATE THE VALUE AND MAKE IT MRU 
        if key in self.cache:
            node = self.cache[key]

            node.value = value
            self.remove(node)
            self.add(node)
            return
        
        # CASE2: NEW VALUE
        if key not in self.cache:          # Case 2: new key

            node = Node(key, value)   # create the new node
            self.cache[key] = node    # add new key into the cache dictionary 

            self.add(node)           # make it MRU

        if len(self.cache)> self.capacity:
            lru = self.head.next
            self.remove(lru)            # Linked List se node hatao
            del self.cache[lru.key]     # Dictionary se entry hatao
        return