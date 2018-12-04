class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxsize=1000000
        self.code = [0] * self.maxsize
        
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.code[key]=1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.code[key]=0
        

    def contains(self, key):    
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.code[key]==1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

a = MyHashSet()
a.add(1)
print(a.contains(1))