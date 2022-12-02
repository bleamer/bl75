class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        validSet = set(['(', ')', '{', '}', '[', ']'])
        for char in s:
            if char in validSet:
                if char == ')' :
                    if  (len(charStack) > 0) and (charStack[-1] != '('):
                        return False
                    else:
                        if (len(charStack) > 0):
                            charStack.pop() 
                            continue
                if char == ']':
                    if (len(charStack) > 0) and (charStack[-1] != '['):
                        return False
                    else:
                        if (len(charStack) > 0):
                            charStack.pop() 
                            continue
                if char == '}' :
                    if (len(charStack) > 0) and (charStack[-1] != '{'):
                        return False
                    else:
                        if (len(charStack) > 0):
                            charStack.pop() 
                            continue
                charStack.append(char)
            else: # do no do anything for other characters
                pass
        if len(charStack) == 0:
            return True
        else:
            return False
        

sol = Solution()
print(sol.isValid("(]"))