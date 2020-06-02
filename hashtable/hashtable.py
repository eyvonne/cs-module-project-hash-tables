class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def set_value(self, value):
        self.value = value

    def set_next(self, key, value):
        self.next = HashTableEntry(key, value)

    def __str__(self):
        return f'key: {self.key}, value: {self.value}, next: {self.next}'

    def __len__(self):
        count = 1
        node = self
        while node.next is not None:
            count += 1
            node = node.next
        return count


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.data = [None] * capacity if capacity >= MIN_CAPACITY else [None] * MIN_CAPACITY
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.data)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return sum([bool(x) for x in self.data]) / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass
        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hash = self.hash_index(key)
        if self.data[hash] is None:
            self.data[hash] = HashTableEntry(key, value)
        else:
            node = self.data[hash]
            while node.next is not None:
                if node.key == key:
                    break
                node = node.next
            if node.key == key:
                node.set_value(value)
            else:
                node.set_next(key, value)
        self.manage_size(hash)  # lets get resize working first then I'll run that code.

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash = self.hash_index(key)
        if self.data[hash] is None:
            print(f'No Data at {key} to delete')
            return None
        elif self.data[hash].key == key:
            if self.data[hash].next == None:
                self.data[hash] = None
            else:
                self.data[hash] = self.data[hash].next
        else:
            node = self.data[hash]
            while node.next.key is not key:
                node = node.next
            node.next = node.next.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash = self.hash_index(key)
        if self.data[hash] is None:
            return None
        elif self.data[hash].key == key:
            return self.data[hash].value
        else:
            node = self.data[hash]
            while node.next is not None:
                if node.key == key:
                    return node.value
                node = node.next
            if node.key == key:
                return node.value
            else:
                return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        data = [x for x in self.data if x is not None]
        self.data = [None] * new_capacity
        self.capacity = new_capacity

        for d in data:
            if d.next is not None:
                node = d
                while node.next is not None:
                    self.put(node.key, node.value)
                    node = node.next
                self.put(node.key, node.value)
            else:
                self.put(d.key, d.value)

    def manage_size(self, index):
        if self.get_load_factor() > .7 or len(self.data[index]) > 3:
            if self.get_load_factor() > .7:
                print(f'load factor increase {self.get_load_factor()}')
            else:
                print(f'length increase {len(self.data[index])}')
            self.resize(self.capacity * 2)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    print(ht.get_num_slots())
    ht.put("line_1", "Did gyre and gimble in the wabe:")
    print(ht.get_num_slots())
    ht.put("line_3", "All mimsy were the borogoves,")
    print(ht.get_num_slots())
    ht.put("line_4", "And the mome raths outgrabe.")
    print(ht.get_num_slots())
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    print(ht.get_num_slots())
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    print(ht.get_num_slots())
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    print(ht.get_num_slots())
    ht.put("line_8", 'The frumious Bandersnatch!"')
    print(ht.get_num_slots())
    ht.put("line_9", "He took his vorpal sword in hand;")
    print(ht.get_num_slots())
    ht.put("line_10", "Long time the manxome foe he sought--")
    print(ht.get_num_slots())
    ht.put("line_11", "So rested he by the Tumtum tree")
    print(ht.get_num_slots())
    ht.put("line_13", "And stood awhile in thought.")
    print(ht.get_num_slots())
    ht.put("line_14", "And stood awhile in thought.")
    print(ht.get_num_slots())
    ht.put("line_15", "And stood awhile in thought.")
    print(ht.get_num_slots())
    ht.put("line_16", "And stood awhile in thought.")
    print(ht.get_num_slots())
    ht.put("line_17", "And stood awhile in thought.")
    print(ht.get_num_slots())
    ht.put("line_18", "And stood awhile in thought.")
    print(ht.get_num_slots())
    ht.put("line_19", "And stood awhile in thought.")
    print(ht.get_num_slots())

    print(ht.get('line_1'))
    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
