#minimum window substring 


from collections import Counter

s = "ADOBECODEBANC"
t = "ABC"
map = Counter(t)
count = len(map)

left = 0
right = 0
min_len = float('inf')
start = 0

while right < len(s):

    # expand window
    char = s[right]

    if char in map:
       map[char] -= 1
       if map[char] == 0:
          count -= 1

    # window valid
    while count == 0:

    # update answer
        if right - left + 1 < min_len:
           min_len = right - left + 1
           start = left

        # shrink window
        char_left = s[left]

        if char_left in map:
           map[char_left] += 1
           if map[char_left] > 0:
              count += 1

        left += 1

    right += 1

if min_len == float('inf'):
  print("")

print(s[start:start + min_len])