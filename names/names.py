import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
'''
SOLUTION
'''
b = BinarySearchTree(names_1[0])
for name_1 in names_1:
    if not name_1 == names_1[0]:
        b.insert(name_1)

for name_2 in names_2:
    if b.contains(name_2):
        duplicates.append(name_2)
    if name_1 == name_2:
        duplicates.append(name_1)

'''
STRETCH PROBLEM ============================================================
'''
# b = []
# for name_1 in names_1:
#     # if not name_1 == names_1[0]:
#     b.append(name_1)
# # print(b)
# for name_2 in names_2:
#     # if b.contains(name_2):
#     #     duplicates.append(name_2)
#     # if name_1 == name_2:
#     #     duplicates.append(name_1)

#     # print(middle, high, low, target)
#     print(name_2)

#     def binarySearch(name_2):
#         low = 0
#         high = len(b)-1
#         target = name_2
#         # TO-DO: add missing code
#         found = 0
#         while low <= high and found == 0:

#             middle = low+(high-1)//2
#             # print(low, high, middle)
#             if target == b[middle]:
#                 print(target)
#                 duplicates.append(name_2)
#                 return True
#             elif b[middle] < target:
#                 low = middle + 1
#             else:
#                 high = middle - 1
#         return False

#     # if binarySearch(name_2):
#     binarySearch(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

'''
first runtime = 8 seconds
first complexity = O(n^2)

My runtime = 0.1 seconds
My complexity = O(n log(n))
'''
