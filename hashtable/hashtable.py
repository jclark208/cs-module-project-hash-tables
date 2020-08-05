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

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.the_list = [None] * capacity



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.the_list)
        


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        count = 0
        for x in self.the_list:
            if x is not None:
                count +=1
                curr_x = x
                while curr_x.next is not None:
                    count += 1
                    curr_x = curr_x.next
        return count/len(self.the_list)



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        offset = 14695981039346656037
        prime = 1099511628211
        key_bytes = key.encode()
        for byte in key_bytes:
            offset *= prime
            offset = offset ^ byte
        return offset % self.capacity


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        
        my_hash = self.fnv1(key)
        my_entry = HashTableEntry(key, value)
        # self.the_list[my_hash] = my_entry
        if self.the_list[my_hash] is not None:
            curr_place = self.the_list[my_hash]
            while curr_place is not None:
                if curr_place.key == key:
                    # print(curr_place.key,key)
                    curr_place.value = value
                    print(curr_place.value,curr_place.key)
                    return
                if curr_place.next is not None:
                    curr_place = curr_place.next
                else:
                    curr_place.next = my_entry
            curr_place.next = my_entry

        else:
            self.the_list[my_hash] = my_entry


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # itterate through the table
        # if found then replace at [i] with None
        # if not found return not found
        my_hash = self.fnv1(key)
        if self.the_list[my_hash]:
            curr_place = self.the_list[my_hash]
            while curr_place.key != key:
                if curr_place.next is not None:
                    curr_place = curr_place.next
                else:
                    return
            curr_place.value = None
            if curr_place.key == key:
                if curr_place.next is not None:
                    self.the_list[my_hash] = curr_place.next
                else:
                    self.the_list[my_hash] = None


        else:
            print("error")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # itterate through the table
        # if found return info at [i]
        # if not found return not found
        my_hash = self.fnv1(key)
        if self.the_list[my_hash] is not None:
            curr_place = self.the_list[my_hash]
            while curr_place.key != key:
                if curr_place.next is not None:
                    curr_place = curr_place.next
                else:
                    return

            return curr_place.value
            
        else:
            print("error")


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # hold on to the what is already in the list
        # set the list to None * new_capacity
        # set the list cap to the new cap
        # loop through the old list and check if item is not NONE
        # if not None add to new storage and save the value of that item.next to current
        # loop through while current still true add current to new storage and change current to current.next
        old_list = self.the_list
        self.the_list = [None] * new_capacity
        self.capacity = new_capacity
        for i in old_list:
            if i is not None:
                self.the_list[self.fnv1(i.key)] = i
                curr_place = i.next
                while curr_place is not None:
                    self.the_list[self.fnv1(curr_place.key)] = curr_place
                    curr_place = curr_place.next





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
