# Design Problem:
# insane problem for a medium LOL:
# Using a linked list and a hasmap to keep track of nodes

class Node:
    def __init__(self, key, val):
        self.key, self.val = key,val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key, node
        
        #dummy pointers connected to each other to store the most and least recent values
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    #helper function to remove a node
    def remove(self, node):
        # just make the previous node point to the next node
        # and the next node point to the previous eliminating the middle node
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    #helper function to insert a node at the right most position
    def insert(self, node):
        #simple insert technique adding pointer to the new node in our current linked list
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt,prev


    def get(self, key: int) -> int:
        if key in self.cache: 
            # if the node is in our cache, we remove it from our list and then 
            # ...reinsert it at our right most position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 # node we are trying to get does not exist in our list


    def put(self, key: int, value: int) -> None:
        # if the key is already in our cache that means there is a node that  
        # exist already in our cache, so we need to remove the old one
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Now we can 'put' this node both in our hashmap and in our doubly linked list
        self.cache[key] = Node(key,value) # insert into hashmap
        self.insert(self.cache[key])      # insert into doubly linked list

        # now check to make sure our cache fits between our capacity limit:
        #if the curr length of the cache exceeds capacity:
        if len(self.cache) > self.cap:
            #get the least recently used (LRU) THE LEFT.NEXT WILL ALWAYS BE THE LRU 
            lru = self.left.next
            #remove it from our linked list
            self.remove(lru)
            #remove it from the hashmap
            del self.cache[lru.key]

