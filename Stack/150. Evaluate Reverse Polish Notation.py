from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        list = '+-*/'
        for x in tokens:

            if x in list:
                val = 0
                match x:
                    case '+':
                        val = stack[-2] + stack[-1]
                    case '-':
                        val = stack[-2] - stack[-1]
                    case '*':
                        val = stack[-2] * stack[-1]
                    case '/':
                        val = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(val))

            else:
                stack.append(int(x))  
            
        return stack.pop()

S = Solution()
print(S.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))