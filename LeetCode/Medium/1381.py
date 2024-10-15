class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.top = -1
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.top == self.maxSize-1:
            return
        self.stack.append(x)
        self.top += 1

    def pop(self) -> int:
        if self.top == -1:
            return -1
        else:
            self.top -= 1
            return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.top+1)):
            self.stack[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
