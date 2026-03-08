#Permutation in String
from collections import Counter
s2 = "eidbaooo"
s1 = "ab"
found = False

k = len(s1)
map = Counter(s1)
count = len(map)
left = 0 
right = 0
        
while right< len(s2):
    if s2[right] in map:
       map[s2[right]]-=1
       if map[s2[right]]==0:
          count -=1
    if right-left+1<k:
       right+=1

    elif right-left+1==k:
       if count == 0:
          found = True
       
       if s2[left]in map:
          map[s2[left]]+=1
          if map[s2[left]]==1:
             count+=1

       left+=1
       right+=1
print(found)
                                 