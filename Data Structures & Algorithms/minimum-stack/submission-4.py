class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
'''
Here we used two stacks, stack and minstack. Stack stores everything where as 
minstack stores every min value seen.
if minstack is empty then the value is added to it too in push function. 
But if its not the case, then the minimum of val and the topmost item in the minstack
is pushed only.
During pop, elements from the stacks are popped 
Push 1: stack = [1]
minStack = [1]
Push 2: stack = [1, 2]
minStack = [1, 1] (min of is 1)
'''