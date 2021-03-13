class QueueViaStacks:
    def __init__(self):
        self.stack = []

    def _isEmpty(self):
        return False if self.stack else True

    def push(self, data):
        print(f'adding {data} to queue')
        self.stack.append(data)

    def pop(self):
        newStack = []
        poppedValue = None

        while self.stack:
            newStack.append(self.stack.pop(-1))

        while newStack:
            if poppedValue == None:
                poppedValue = newStack.pop(-1)
            else:
                self.stack.append(newStack.pop(-1))

        return poppedValue


if __name__ == '__main__':
    queue = QueueViaStacks()
    for i in range(9):
        queue.push(i)

    print()
    while not queue._isEmpty():
        print(f'popping {queue.pop()} from the queue')
