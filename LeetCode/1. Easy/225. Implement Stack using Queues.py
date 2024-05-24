class MyStack:

    def __init__(self):
        self.stack:list = []

    def push(self, x: int) -> None:
        if x not in self.stack:
            self.stack.append(x)
        else:
            self.stack.remove(x)
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) != 0:
            temptopo = self.stack.pop(-1)

        return temptopo

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()