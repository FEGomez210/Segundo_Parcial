class HeapMin:
    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def arrive(self, item, priority):
        self.elements.append([priority, item])
        self._sift_up(len(self.elements) - 1)

    def attention(self):
        if not self.elements:
            return None
        min_item = self.elements[0]
        last = self.elements.pop()
        if self.elements:
            self.elements[0] = last
            self._sift_down(0)
        return min_item

    def search(self, value):
        for i, elem in enumerate(self.elements):
            try:
                if elem[1][0] == value:
                    return i
            except Exception:
                continue
        return None

    def change_priority(self, pos, new_priority):
        if pos < 0 or pos >= len(self.elements):
            return
        old = self.elements[pos][0]
        self.elements[pos][0] = new_priority
        if new_priority < old:
            self._sift_up(pos)
        else:
            self._sift_down(pos)

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.elements[idx][0] < self.elements[parent][0]:
                self.elements[idx], self.elements[parent] = self.elements[parent], self.elements[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.elements)
        while True:
            left = 2 * idx + 1
            right = left + 1
            smallest = idx
            if left < n and self.elements[left][0] < self.elements[smallest][0]:
                smallest = left
            if right < n and self.elements[right][0] < self.elements[smallest][0]:
                smallest = right
            if smallest != idx:
                self.elements[idx], self.elements[smallest] = self.elements[smallest], self.elements[idx]
                idx = smallest
            else:
                break
