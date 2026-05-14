"""
155. 最小栈
"""

class MinStack:

    def __init__(self):
        self.st = []
        self.m = []
        
    def push(self, val: int) -> None:
        if not self.m or self.m[-1] >= val:
            self.m.append(val)
        
        self.st.append(val)

    def pop(self) -> None:
        if self.st.pop() == self.m[-1]:
            self.m.pop()
        
    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.m[-1]