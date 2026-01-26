# shoring based on two arrays

a=[1,4,6,9,10]
b=[10,16,19,21,22,24]
n = len(a)
m = len(b)
left = 0
right = 0
result =[]
while left < n and right < m:
   if a[left]<b[right]:
      result.append(a[left])
      left = left + 1
      
   else:
      result.append(b[right])
      right = right+1

while left < n:
   result.append(a[left])
   left = left +1
while right < m:
   result.append(b[right])
   right =right+1

print(result)   



      