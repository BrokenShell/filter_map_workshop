""" Four flavors of map
All 4 produce the exact same output.
The first two are ugly and considered by most to be non-Pythonic. """
from main import add_one

arr = list(range(10))
print(arr)

# 1. This is particularly ugly - don't do this, avoid indexing when you can
looped_arr = []
for i in range(len(arr)):
    looped_arr.append(add_one(arr[i]))
print(looped_arr)

# 2. This is slightly less ugly - don't do this either, unless you have to
looped_arr2 = []
for val in arr:
    looped_arr2.append(add_one(val))
print(looped_arr2)

# 3. This is beautiful and what most hiring managers want to see
mapped_arr = list(map(add_one, arr))
print(mapped_arr)

# 4. This is very beautiful and my preferred methodology
comp_arr = [add_one(val) for val in arr]
print(comp_arr)
