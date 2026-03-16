#Substrings of Size Three with Distinct Characters
s ="xyzzaz"
n = len(s)
left = 0
right = 0 
count = 0
k = 3

while right<n:
  if right-left+1<k:
    right+=1

  elif right-left+1 == k:
    if len(set(s[left:right+1])) == k:  # left:right+1 --> represent string 
       count+=1

    left+=1
    right+=1

print (count)                      