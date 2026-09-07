class Solution:
    def calPoints(self, operations: List[str]) -> int:
        resStack = []
        for op in operations:
            if op == 'C' and resStack:
                resStack.pop()
            elif op == 'D' and resStack:
                lastValue =  resStack[-1]
                resStack.append(lastValue*2)
            elif op == '+' and len(resStack)>=2:
                first = resStack[-2]
                second =  resStack[-1]
                resStack.append(first+second)
            else:
                resStack.append(int(op))
        
        return sum(resStack)
                
