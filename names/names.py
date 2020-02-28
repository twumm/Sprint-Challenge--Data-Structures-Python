import time
from binary_search_tree import BinarySearchTree
import sys
sys.path.append('../names')

start_time = time.time()
# start_time = time.process_time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# initialize and add first value to BinarySearchTree
bst_names = BinarySearchTree(names_1[0])
# go through names and insert into tree
for name in names_1:
    bst_names.insert(name)

# loop through 2nd names list
for name in names_2:
    # check if bst_names contains the name
    if bst_names.contains(name):
        # append the duplicated names
        duplicates.append(name)

""" Old code that takes 22 secs """
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
