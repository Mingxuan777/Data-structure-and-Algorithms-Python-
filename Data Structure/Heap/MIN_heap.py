class Array(object):
    def __init__(self, size = 32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value = None):
        for i in range(self._size):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

class MINHeap(object):
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[parent] > self._elements[ndx]:
                self._elements[parent], self._elements[ndx] = self._elements[ndx], self._elements[parent]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        if ndx < self._count:
            left = 2 * ndx + 1
            right = 2 * ndx + 1
            if (left < self._count and right < self._count \
                    and self._elements[left] <= self._elements[right] \
                    and self._elements[left] <= self._elements[ndx]):
                self._elements[left], self._elements[ndx] = self._elements[ndx], self._elements[left]
            elif left < self._count and right < self._count \
                    and self._elements[left] >= self._elements[right] \
                    and self._elements[right] <= self._elements[ndx]:
                self._elements[right], self._elements[ndx] = self._elements[ndx], self._elements[right]
            
            if left < self._count and right > self._count \ 
                    and self._elements[left] <= self._elements[ndx]:
                self._elements[left], self._elements[ndx] = self._elements[ndx], self._elements[left]
                self._siftdown(left)

def test_maxheap():
    import random
    n = 5
    h = MINHeap(n)
    for i in range(0, n):
        h.add(i)
    for i in reversed(range(0, n)):
        assert i == h.extract()

