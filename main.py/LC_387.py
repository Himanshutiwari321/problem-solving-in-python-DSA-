# find unique character in a string 

s = "leetcode"

ans= {}

for i in s:
  if i not in ans:
     ans[i]=1

  else:
     ans[i]+=1

for ch in range (len(s)):
   if ans[s[ch]]==1:
      print(s[ch])
      #print(ch)
      break
else:  
  print(-1)          





