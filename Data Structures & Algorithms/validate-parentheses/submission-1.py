class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        required = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        for bracket in s:
            if bracket in required:
                if len(stack) > 0 and stack[-1] == required[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return not stack