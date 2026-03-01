#Find All Anagrams in a String


from collections import Counter

s = "cbaebabacd"
p = "abc"

k = len(p)
map = Counter(p)     # frequency of pattern
count = len(map)     # number of unique characters
left = 0
right =0
#ans = []
ans = 0
while right< len(s):

# Step 1: include right character
    if s[right] in map:
       map[s[right]] -= 1
       if map[s[right]] == 0:
          count -= 1

# Step 2: when window size < k
    if right - left + 1 < k:
       right+=1

# Step 3: when window size == k
    elif right - left + 1 == k:

       if count == 0:
          #ans.append(left)
          ans+=1

# remove left character (slide window)
       if s[left] in map:         
          map[s[left]] += 1
          if map[s[left]] == 1:
            count += 1

       left += 1
       right+=1

print(ans)