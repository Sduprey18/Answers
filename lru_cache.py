class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.head = Node("head", -1)
        self.tail = Node("tail", -2)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            #move to front, since its the most recelntly used
            print(f"Moving {self.cache[key].value} to the front")
            self.moveToFront(self.cache[key])
            #return the value of the node (the val in the dict will be the nodes)
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
        # then put it to the front
            self.moveToFront(self.cache[key])
        else:
            
            if len(self.cache) == self.capacity:
                nodeToRemove = self.tail.prev
                print(f"ok removing node {nodeToRemove.value}")
                
                self.remove(nodeToRemove)
                self.tail.prev = nodeToRemove.prev
                #print(self.cache)
                keyToRemove = nodeToRemove.key
                del self.cache[keyToRemove]
                print(f"succesfully removed {nodeToRemove.value}, length is now {len(self.cache)}")
            
            node = Node(value, key)
            self.cache[key] = node
            # then put it to the front
            self.moveToFront(self.cache[key])
            print(f"We just put in {node.value}")


    
    def remove(self, node):
        #print(f"ok removing node {node.value}")
        prev, _next = node.prev, node.next
        prev.next = _next
        _next.prev = prev
    
    '''
    want to move 5 to front
    head <-> (5) -> 3 <->  <-> tail
    oldnext = tail, oldfront = 3
     
    '''
    def moveToFront(self, node):
        #remove the node first
        if node.prev is not None and node.next is not None:
        
            self.remove(node)

        #change head and next pointer then
        oldNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = oldNext
        if oldNext:
            oldNext.prev = node
