from collections import deque
class AnimalShelter(object):
    def __init__(self):
        # do some intialize if necessary
        self.dogs = deque([])
        self.cats = deque([])
        self.order = 0
    """
    @param {string} name
    @param {int} type, 1 if Animal is dog or 0
    @return nothing
    """
    def enqueue(self, name, type):
        # Write yout code here
        if type == 1:
            self.dogs.append((name, self.order))
            self.order += 1
        elif type == 0:
            self.cats.append((name, self.order))
            self.order += 1

    # return a string
    def dequeueAny(self):
        # Write your code here
        if not self.dogs and not self.cats:
            return None
        if not self.dogs:
            cat = self.cats.popleft()
            return cat[0]
        if not self.cats:
            dog = self.dogs.popleft()
            return dog[0]
        dog = self.dogs[0]
        cat = self.cats[0]
        if dog[1] > cat[1]:
            self.cats.popleft()
            return cat[0]
        else:
            self.dogs.popleft()
            return dog[0]

    # return a string
    def dequeueDog(self):
        # Write your code here
        if self.dogs:
            dog = self.dogs.popleft()
            return dog[0]
        else:
            return None

    # return a string
    def dequeueCat(self):
        # Write your code here
        if self.cats:
            cat = self.cats.popleft()
            return cat[0]
        else:
            return None