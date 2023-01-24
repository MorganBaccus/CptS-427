import pandas as pd
from itertools import product
import hashlib

# save words as a list of strings for passwords
df = pd.read_csv("wordList.csv",header=None)
passwords = df[df.columns[0]].tolist()

# save words as a list of strings for salts
df = pd.read_csv("wordList.csv",header=None)
salts = df[df.columns[0]].tolist()

# save hashed passwords as a set
df = pd.read_csv("Password-1.csv",header=None)
hashs = set(df[df.columns[4]].tolist())
#print(hashs)

# create a list of tuples of every combo of passwords and salts
combinations = list(product(passwords, salts))

combos_with_hash = []

for original_tuple in combinations:
    combined_string = str(original_tuple[0]) + str(original_tuple[1])

    # encode the string to bytes
    encoded_tuple = combined_string.encode()

    # create an md5 hash object
    hash_object = hashlib.md5()

    # update the hash object with the bytes-like object
    hash_object.update(encoded_tuple)

    # get the hexadecimal representation of the hash
    md5_hash = hash_object.hexdigest()

    new_tuple = tuple(list(original_tuple) + [md5_hash])

    if md5_hash in hashs:
        # append new tuple with hash to the list
        combos_with_hash.append(new_tuple)

print(combos_with_hash)

# create a dataframe from the data
df = pd.DataFrame(combos_with_hash, columns=['Password', 'Salt', 'Hash'])

# write the dataframe to a CSV file
df.to_csv("output.csv", index=False)
