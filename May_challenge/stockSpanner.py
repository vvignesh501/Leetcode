class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


g = StockSpanner().next([[],[100],[80],[60],[70],[60],[75],[85]])
print(g)