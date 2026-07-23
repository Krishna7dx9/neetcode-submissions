class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operators:     # it means it is a number
                stack.append(int(token))
            else:                          # means it is operator
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                else:
                    result = int(left / right)
                stack.append(result)

        return stack[-1]