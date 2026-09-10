class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+" and len(stack)>=2:
                stack.append(stack.pop()+stack.pop())
            elif t == "*" and len(stack)>=2:
                stack.append(stack.pop()*stack.pop())
            elif t == "-" and len(stack)>=2:
                first,second = stack.pop(),stack.pop() 
                stack.append(second - first)
            elif t == "/" and len(stack)>=2:
                first,second =  stack.pop(),stack.pop()
                stack.append(int(second/first))
            else:
                stack.append(int(t))
        
        return stack[-1]