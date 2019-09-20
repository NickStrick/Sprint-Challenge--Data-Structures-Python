class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current >= self.capacity:
            self.current = 0
        self.storage[self.current] = item
        self.current += 1

    def get(self):

        return list(filter(lambda x: x != None, self.storage))


buffer = RingBuffer(5)

print(len(buffer.storage), 5)
print(buffer.storage, 5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.storage, 5)
print(buffer.get(), ['a', 'b', 'c', 'd'])

buffer.append('e')
print((buffer.storage), 5)
buffer.append('f')
print((buffer.storage), 5)
