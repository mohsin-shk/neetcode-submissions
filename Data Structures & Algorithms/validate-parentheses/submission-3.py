class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for i in range(len(s)):
        #     if s[i] == '(' or s[i]== '[' or s[i]=='{':
        #         stack.append(s[i])
        #     else:
        #         if not stack:
        #             return False
        #         if((s[i]==')' and stack[-1]=='(') or (s[i]==']' and stack[-1]=='[') or (s[i]=='}' and stack[-1]=='{')):
        #             stack.pop()
        #         else:
        #             return False
        

        # return len(stack)==0

        # much cleaner code:
        stack = []
        closeToOpen = {")":"(","}":"{","]":"["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        

        return True if not stack else False
