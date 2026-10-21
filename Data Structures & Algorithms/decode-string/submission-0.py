class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i]!=']':     
                stack.append(s[i])
            else:
                sub = ''
                while stack[-1]!='[':
                    sub = stack.pop() + sub 
                # poping the '[' as well
                stack.pop()

                mul = ''
                while stack and stack[-1].isdigit():
                    mul = stack.pop() + mul
    
                # we have the mul and sub but in reverse
                stack.append(int(mul)*sub)

        return "".join(stack)