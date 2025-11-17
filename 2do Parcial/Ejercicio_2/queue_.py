class Queue:
    def __init__(self):
        self._items = []

    def arrive(self, item):
        self._items.append(item)

    def attention(self):
        if not self._items:
            return None
        return self._items.pop(0)

    def size(self):
        return len(self._items)
