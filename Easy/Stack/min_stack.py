class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.small = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        if not self.small:
            self.small.append(x)
        else:
            if x <= self.small[-1]:
                self.small.append(x)
        return None

    def pop(self):
        """
        :rtype: None
        """
        if self.items:
            if self.items.pop() == self.small[-1]:
                self.small.pop()
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.small:
            return self.small[-1]
        else:
            return None



obj = MinStack()
obj.push([[],[1],[2]])
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()