""" Three flavors of filter
All 3 produce the exact same output.
The first one is ugly and considered by most to be non-Pythonic. """
from main import is_odd

arr = list(range(10))
print(arr)

# 1. This is ugly - just don't
looped = []
for val in arr:
    if is_odd(val):
        looped.append(val)
print(looped)

# 2. This is beautiful and what most hiring managers want to see
filtered_arr = list(filter(is_odd, arr))
print(filtered_arr)

# 3. This is very beautiful and my preferred methodology
comp_arr = [val for val in arr if is_odd(val)]
print(comp_arr)
