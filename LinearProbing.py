class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # Open addressing
        self.entries = 0

    def _hash(self, key, i):
        return (hash(key) + i) % self.size

    def insert(self, key, value):
        for i in range(self.size):
            idx = self._hash(key, i)
            if self.table[idx] is None or self.table[idx][0] == key:
                if self.table[idx] is None:
                    self.entries += 1
                self.table[idx] = (key, value)
                return
        raise Exception("Table full")

    def search(self, key):
        probes = 0
        for i in range(self.size):
            idx = self._hash(key, i)
            probes += 1
            entry = self.table[idx]
            if entry is None:
                return None, probes
            if entry[0] == key:
                return entry[1], probes
        return None, probes

    def delete(self, key):
        for i in range(self.size):
            idx = self._hash(key, i)
            entry = self.table[idx]
            if entry is None:
                break
            if entry[0] == key:
                self.table[idx] = None  # Tombstone
                self.entries -= 1
                return
        raise KeyError(f"Key {key} not found")

    def load_factor(self):
        return self.entries / self.size

# Example Usage
ht_lp = HashTableLinearProbing()
ht_lp.insert("apple", 5)
ht_lp.insert("banana", 10)
ht_lp.insert("cherry", 15)  # Collision resolved via linear probing
print(ht_lp.search("cherry"))  # (15, 3 probes)
print(f"Load Factor: {ht_lp.load_factor()}")  # 0.3