class HashTableSeparateChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists
        self.entries = 0

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        bucket.append((key, value))
        self.entries += 1

    def search(self, key):
        idx = self._hash(key)
        probes = 0
        for k, v in self.table[idx]:
            probes += 1
            if k == key:
                return v, probes
        return None, probes

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.entries -= 1
                return
        raise KeyError(f"Key {key} not found")

    def load_factor(self):
        return self.entries / self.size

# Example Usage
ht_sc = HashTableSeparateChaining()
ht_sc.insert("apple", 5)
ht_sc.insert("banana", 10)
ht_sc.insert("cherry", 15)  # Collision handled via chaining
print(ht_sc.search("banana"))  # (10, 1 probe)
print(f"Load Factor: {ht_sc.load_factor()}")  # 0.3