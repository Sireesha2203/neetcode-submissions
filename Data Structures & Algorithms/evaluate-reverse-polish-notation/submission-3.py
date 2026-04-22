class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=['+', '-', '*', '/']
        stack=[]
        for i in tokens:
            if i in op :
                t1=stack.pop()
                t2=stack.pop()
                if i=='+':
                    t=t1+t2 
                elif i=='-':
                    t=t2-t1 
                elif i=='*':
                    t=t1*t2 
                else:
                    t=int(t2 / t1) 
                stack.append(t)
            else:
                stack.append(int(i))
        return stack.pop()

