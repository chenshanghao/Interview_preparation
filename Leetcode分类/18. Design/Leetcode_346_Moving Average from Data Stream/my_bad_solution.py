class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = []
        self.count = 0
        self.size = size
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if self.count < self.size:
            self.queue.append(val)
            self.count += 1
            return sum(self.queue) * 1.0 / self.count
        else:
            self.queue.pop(0)
            self.queue.append(val)
            return sum(self.queue) * 1.0 / self.count
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)