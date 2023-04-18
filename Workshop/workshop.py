class HashTable:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        self.data = [None] * self.DEFAULT_CAPACITY

    def add(self, key, value):
        idx = self.calc_idx(key)
        if self.data[idx] is None:
            self.data[idx] = [(key, value)]
            return
        for k, _ in self.datap[idx]:
            if key == k:
                raise KeyError
        self.data[idx].append((key, value))

    def get(self, key):
        idx = self.calc_idx(key)
        idx_elements = self.data[idx]
        if idx_elements is None:
            raise KeyError

        for k, v in idx_elements:
            if k == key:
                return v
        raise KeyError

    def remove(self, key):
        idx = self.calc_idx(key)
        idx_elements = self.data[idx]
        if idx_elements is None:
            raise KeyError

        for k, v in idx_elements:
            if k == key:
                self.data[idx].remove((k, v))
                return

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        pass

    def calc_idx(self, key):
        return hash(key) % len(self.data)
