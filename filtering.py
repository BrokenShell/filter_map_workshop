""" Three flavors of filter
All 3 produce the exact same output.
The first one is ugly and considered by most to be non-Pythonic. """
from main import is_odd

arr = list(range(10))
print(arr)

# 1. This is particularly ugly - don't do this, always avoid indexing
looped_arr = []
for i in range(len(arr)):
    if is_odd(arr[i]):
        looped_arr.append(arr[i])
print(looped_arr)

# 2. This is slightly less ugly - don't do this either
looped_arr2 = []
for val in arr:
    if is_odd(val):
        looped_arr2.append(val)
print(looped_arr2)

# 3. This is beautiful and what most hiring managers want to see
filtered_arr = list(filter(is_odd, arr))
print(filtered_arr)

# 4. This is very beautiful and my preferred methodology
comp_arr = [val for val in arr if is_odd(val)]
print(comp_arr)
