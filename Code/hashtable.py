#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) where n is equal to the average number
        of items in a bucket
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) where n is equal to the average number
        of items in a bucket
        """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) where n is equal to the average number
        of items in a bucket"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items()) # bucket.items() = O(l)
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) where n is equal to the average number
        of items in a bucket"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0 #O(1)
        for bucket in self.buckets: # b iterations => O(b*l) = O(n)
            count += bucket.length() # O(l) for length method where l is n/b
        return count # O(1)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: Best case O(1) if it's found at the first item in the bucket
        Worst case O(l) where l is equal to the number of items in the bucket.
        Worst case if it's the last item in the bucket or not found at all
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        item = bucket.find(lambda value: value[0] == key) # best case O(1), worst case O(l) where l is n/b

        if item == None: # O(1)
            return False # O(1)
        else:
            return True # O(1)


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: Best case O(1) if it's found at the first item in the bucket
        Worst case O(l) where l is equal to the number of items in the bucket.
        Worst case if it's the last item in the bucket or not found at all"""

        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        # TODO: Check if key-value entry exists in bucket
        item = bucket.find(lambda value: value[0] == key) # best case O(1), worst case O(l) where l is n/b

        if item == None: # O(1)
            # TODO: Otherwise, raise error to tell user get failed
            raise KeyError('Key not found: {}'.format(key))
        else:
            # TODO: If found, return value associated with given key
            return item[1] # O(1)


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: Best case O(1) if it's found at the first item in the bucket
        Worst case O(l) where l is equal to the number of items in the bucket.
        Worst case if it's the last item in the bucket or not found at all"""


        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        # TODO: Check if key-value entry exists in bucket
        item = bucket.find(lambda value: value[0] == key) # best case O(1), worst case O(l) where l is n/b

        if item == None: # O(1)
            # Not found, insert given key-value entry into bucket
            bucket.append((key, value)) # O(1)
        else:
            # Found, update value associated with given key
            bucket.delete(item) # best case O(1), worst case O(l) where l is n/b
            bucket.append((key, value)) # O(1)


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: Best case O(1) if it's found at the first item in the bucket
        Worst case O(l) where l is equal to the number of items in the bucket.
        Worst case if it's the last item in the bucket or not found at all"""

        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        # TODO: Check if key-value entry exists in bucket
        item = bucket.find(lambda value: value[0] == key) # best case O(1), worst case O(l) where l is n/b

        if item == None: # O(1)
            # Not Found, raise error to tell user delete failed
            raise KeyError('Key not found: {}'.format(key))
        else:
            # Found, delete entry associated with given key
            bucket.delete(item) # best case O(1), worst case O(l) where l is n/b


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
