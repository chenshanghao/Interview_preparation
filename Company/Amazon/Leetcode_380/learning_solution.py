import random

class RandomizedSet(object):

    def __init__(self):
        # do initialize if necessary    
        self.nums, self.pos = [], {}
        
    # @param {int} val Inserts a value to the set
    # Returns {bool} true if the set did not already contain the specified element or false
    def insert(self, val):
        # Write your code here
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        
    # @param {int} val Removes a value from the set
    # Return {bool} true if the set contained the specified element or false
    def remove(self, val):
        # Write your code here
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop()
            del self.pos[val]
            return True
        return False
    
    # return {int} a random number from the set
    def getRandom(self):
        # Write your code here
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()