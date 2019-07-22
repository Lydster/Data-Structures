class Queue:
    def __init__(self):
        self.size = 0

        # what data structure should we
        # use to store queue elements?
        self.storage = list()

    def enqueue(self, item):
        if item not in self.storage:
            self.storage.insert(0, item)
            return True
        return False

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop()
        return None

    def len(self):
        return len(self.storage)
