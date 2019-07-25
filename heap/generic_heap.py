class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.insert(len(self.storage), value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        s = self.storage
        s[0], s[len(s) - 1] = s[len(s) - 1], s[0]
        max = s.pop(len(s) - 1)
        self._sift_down(0)
        return max

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                index = parent
            else:
                break

    def _sift_down(self, index):
        if 2 * index + 1 > len(self.storage) - 1:
            return
        elif (2 * index) + 2 > len(self.storage) - 1 or self.comparator(self.storage[2 * index + 1], self.storage[2 * index + 2]):
            if not self.comparator(self.storage[index], self.storage[2 * index + 1]):
                self.storage[index], self.storage[2 * index +
                                                  1] = self.storage[2 * index + 1], self.storage[index]
                self._sift_down(2 * index + 1)
            else:
                return
        else:
            if not self.comparator(self.storage[index], self.storage[2 * index + 2]):
                self.storage[index], self.storage[2 * index +
                                                  2] = self.storage[2 * index + 2], self.storage[index]
                self._sift_down(2 * index + 2)
            else:
                return
