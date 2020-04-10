#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        # variable to be checked in hashtable
        j = hash_table_retrieve(ht, limit - weights[i])

        # check hashtable for None then insert key value pair
        if j is None:
            hash_table_insert(ht, weights[i], i)
        
        else:
            return (i, j)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
