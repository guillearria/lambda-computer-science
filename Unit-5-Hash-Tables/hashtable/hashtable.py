class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        LF > 0.7 = OVERLOADED
        LF < 0.2 = UNDERLOADED

        Implement this.
        """
        # lf = (num of elements) /(num of slots)
        load_factor = self.load/self.capacity

        return load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.

        algorithm fnv-1 is
            hash := FNV_offset_basis

            for each byte_of_data to be hashed do
                hash := hash × FNV_prime
                hash := hash XOR byte_of_data

            # XOR = BITWISE EXCLUSIVE = ^

            return hash

        FNV_offset_basis, 64-bit FNV offset basis value: 14695981039346656037
            (in hex, 0xcbf29ce484222325).
        FNV_prime, 64-bit FNV prime value: 1099511628211
            (in hex, 0x100000001b3).

        Start at FNV_offset_basis,
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hash_val = FNV_offset_basis

        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            hash_val = hash_val * FNV_prime
            hash_val = hash_val ^ byte  # XOR = BITWISE EXCLUSIVE OPERATOR

        return hash_val

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.

        unsigned long
        hash(unsigned char *str)
        {
            unsigned long hash = 5381;
            int c;

            while (c = *str++)
                hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

            return hash;
        }

        x << y: Returns x with the bits shifted to the left by y places
            (and new bits on the right-hand-side are zeros).
            This, same as multiplying x by 2**y.
        """
        hash_val = 5381  # unsigned long hash
        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            hash_val = ((hash_val << 5) + byte)

        return hash_val

        # SIMILAR:
        # for x in key:
        #     hash = ((hash << 5) + hash) + ord(x)

        # return hash & 0xFFFFFFFF

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
            * One LL per index, each node points to the next..
            * Python uses "open addressing" or "linear probing"

        Implement this.
        """
        # check load factor, resize if necessary
        lf = self.get_load_factor()

        if lf >= 0.7:
            # num slots = num load/lf
            ideal_capacity = int(self.load+1//lf)
            self.resize(ideal_capacity)

        # turn key into an index, include modulo
        idx = self.hash_index(key)
        cur_node = self.storage[idx]

        # check for collision
        if cur_node:
            # replace value if key exists
            if cur_node.key == key:
                cur_node.value = value
            else:
                # while the next node is not None, iterate to next node
                while cur_node.next:
                    # replace value if key exists
                    if cur_node.next.key == key:
                        cur_node.next.value = value
                        return
                    else:
                        cur_node = cur_node.next
                # when next node is None, replace None with new entry
                cur_node.next = HashTableEntry(key, value)
                self.load += 1
        else:
            # put value at that index in hash table array
            self.storage[idx] = HashTableEntry(key, value)
            self.load += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # turn key into an index, include modulo
        idx = self.hash_index(key)
        cur_node = self.storage[idx]
        node_deleted = False

        if cur_node.key == key:
            if cur_node.next:
                self.storage[idx] = cur_node.next
            else:
                self.storage[idx] = None
            node_deleted = True
        else:
            while cur_node.next:
                if cur_node.next.key == key:
                    if cur_node.next.next:
                        cur_node.next = cur_node.next.next
                    else:
                        cur_node.next = None
                    node_deleted = True
                    break
                else:
                    cur_node = cur_node.next

        if node_deleted:
            self.load -= 1
        else:
            print(f"Warning: {key} key does not exist")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # turn key into an index
        idx = self.hash_index(key)
        cur_node = self.storage[idx]

        # if cur node is an entry, check key
        if cur_node:
            if cur_node.key == key:
                return cur_node.value
            # if not given key, check LL
            else:
                while cur_node.next:
                    if cur_node.next.key == key:
                        return cur_node.next.value
                    else:
                        cur_node = cur_node.next
                # if no key match is found, return None
                return None
        # if cur node is None return None
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # duplicate current storage
        old_storage = self.storage.copy()

        # update resized hashtable
        self.capacity = new_capacity
        self.storage = [None] * new_capacity
        self.load = 0

        # iterate down old storage, put to new
        for entry in old_storage:
            cur_node = entry
            while cur_node:
                self.put(cur_node.key, cur_node.value)
                cur_node = cur_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
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
