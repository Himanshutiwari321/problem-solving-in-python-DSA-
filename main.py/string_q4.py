# remove duplicate characters in a string ,given string is s="programmming" .

s="programming"
result = ""

for ch in s :
  if ch not in result:
     result = result + ch 

print (result)   
