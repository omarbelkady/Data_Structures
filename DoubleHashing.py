class HashTableDoubleHashing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.entries = 0

    def _hash1(self, key):
        return hash(key) % self.size

    def _hash2(self, key):
        # Ensure hash2 is never 0 and coprime with size
        h = hash(key) % (self.size - 1)
        return 1 + h if h == 0 else h

    def _probe(self, key, i):
        return (self._hash1(key) + i * self._hash2(key)) % self.size

    def insert(self, key, value):
        for i in range(self.size):
            idx = self._probe(key, i)
            if self.table[idx] is None or self.table[idx][0] == key:
                if self.table[idx] is None:
                    self.entries += 1
                self.table[idx] = (key, value)
                return
        raise Exception("Table full")

    def search(self, key):
        probes = 0
        for i in range(self.size):
            idx = self._probe(key, i)
            probes += 1
            entry = self.table[idx]
            if entry is None:
                return None, probes
            if entry[0] == key:
                return entry[1], probes
        return None, probes

    def load_factor(self):
        return self.entries / self.size

# Example Usage
ht_dh = HashTableDoubleHashing()
ht_dh.insert("apple", 5)
ht_dh.insert("banana", 10)
ht_dh.insert("cherry", 15)  # Collision resolved via double hashing
print(ht_dh.search("cherry"))  # (15, 2 probes)
print(f"Load Factor: {ht_dh.load_factor()}")  # 0.3