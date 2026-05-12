class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            
            if token == '+' or token == '-' or token == '*' or token == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                if token =='+':
                    result = num1+num2
                elif token == '-':
                    result = num1-num2
                elif token =='*':
                    result = num1*num2
                elif token =='/':
                    result = int(num1/num2)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]


