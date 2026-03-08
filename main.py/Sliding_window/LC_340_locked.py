#Longest substring or k distinct (unique) characters 
s = "aabacbebebe"
k = 3  #unique characters should be in your string 


n = len (s)
max_len = 0
left = 0
right  = 0

map ={}

while right < n:
    char = s[right]
    if char in map :
        map[char]+=1
    else:
        map[char]=1

    if len(map)==k:
        max_len =max(max_len, right- left+1)


    while len(map) > k:
        char_left = s[left]
        map[char_left] -=1
        if map[char_left]==0:
           del map[char_left]
        left+=1

    right +=1

print(max_len)            






 