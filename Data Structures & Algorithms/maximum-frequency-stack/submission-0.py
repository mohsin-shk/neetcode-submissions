class FreqStack:

    def __init__(self):
        self.maxCnt = 0
        self.HashMap = {}
        self.stacks = {}

    def push(self, val: int) -> None:
        valCnt  = 1 + self.HashMap.get(val,0)
        self.HashMap[val] = valCnt
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res =  self.stacks[self.maxCnt].pop()
        self.HashMap[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()