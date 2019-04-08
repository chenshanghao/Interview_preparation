class StackofPlates:
    def __init__(self, capacity):
        # Set main stack
        self.stacks = []
        if capacity < 1:
            raise NameError(" A stack is greater than one.")
        else:
            self.capacity = capacity

    def push(self, item):
        # Stack to be pushed to main stack
        # If main stack is empty
        if self.stack = []:
            #  append new stack/array with item to main stack
            self.stacks.append([item])
        else:
            #  if length of last stack/array in main stack is
            #  greater than or equal to self.capacity
            if len(self.stacks[-1]) >= self.capacity:
                # append that item to main stack with
                # a new stack/array
                self.stacks.append([item])
            else:
                # else append item to end of inner stack
                self.stacks[-1].append(item)

    def pop(self):
        if self.stack == []:
            raise NameError("Can't pop an empty stack")
        else:
            # store last item in stack (not last array) into poped data

        popped_data = self.stack[-1][-1]
        # if length of last stack/array equals 1
        # For example: [[1,2,3],[4,5,6],[7]]
        if len(self.stacks[-1]) == 1:
            # delete last stack/array  New array[[1,2,3],[4,5,6]]
            del self.stacks[-1]
        else:
            # if length of last stack/array is greater
            # than 1. For example: [[1,2,3], [4,5,6],[7,8,9]]
            del self.stacks[-1][-1]
        return poped_data

    # Pops last element in sub stack
    def popAt(self, index):
        # if empty stack
        if self.stacks == []:
            raise NameError("can't pop an empty stack")
        elif index-1 > len(self.stacks):
            raise NameError("index is out of range")

        # pops the last element in selected index of main stack
        popped_data = self.stacks[index - 1][-1]
        if len(self.stacks[index - 1]) == 1:
            # if stack length equals one just delete the last element
            del self.stacks[-1]
        elif len(self.stacks) == index:
            del self.stacks[-1][-1]
        else:
            self.stacks[index-1][-1] = self.stacks[index][0]

            for i in range(index, len(self.stacks)):
                # move each element forward/up
                for j in range(0, len(self.stacks[i])-1):
                    self.stacks[i][j] = self.stacks[i][j+1]
                if i<len(self.stacks) - 1:
                    self.stacks[i][-1] = self.stacks[i+1][0]
            del self.stacks[-1][-1]
            # if length of stack is empty. delete it
            if len(self.stacks[-1]) == 0:
                del self.stacks[-1]
        return poped_data


































