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
        return sum([bool(x) for x in self.data]) / len(self.data)

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
                    node.set_value(value)
                    return None
                node = node.next
            if node.key == key:
                node.set_value(value)
                return None
            else:
                node.set_next(key, value)
        # print(*self.data, sep='; ')

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
        print(f'getting key {key}', end=', ')
        hash = self.hash_index(key)
        if self.data[hash] is None:
            return None
        elif self.data[hash].key == key:
            print(f'returning {self.data[hash].value}')
            return self.data[hash].value
        else:
            node = self.data[hash]
            while node.next is not None:
                if node.key == key:
                    print(f'returning {node.value}')
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
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_1", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    print(ht.data[5])
    print(ht.get('line_1'))
    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()
    #
    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
    #
    # print("")
