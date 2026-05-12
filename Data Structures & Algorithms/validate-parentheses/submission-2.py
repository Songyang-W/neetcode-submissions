class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        
        for b in s:
            if b in close_to_open:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if top == close_to_open[b]:
                    continue
                else:
                    return False
            else:
                stack.append(b)
        if len(stack)==0:
            return True
        else:
            return False
