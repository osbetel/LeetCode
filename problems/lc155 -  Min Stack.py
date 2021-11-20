# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:
    def __init__(self):
        self.data = []
        self.min = None

    def push(self, x):
        self.data.append(x)
        if self.min == None: self.min = x
        elif x < self.min: self.min = x


    def pop(self):
        p = self.data.pop()
        if self.data == []:
            self.min = None
        if self.min == p:
            self.newMin()
        return p


    def top(self):
        if self.data == []: return None
        return self.data[len(self.data) - 1]


    def getMin(self):
        if self.data == []: return None
        return self.min


    def newMin(self):
        # only executed if the min is on top of the stack and it is popped off
        self.min = min(self.data)
