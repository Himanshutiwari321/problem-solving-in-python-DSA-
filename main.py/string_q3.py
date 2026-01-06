#how many vowels and con in string count and print, given string is S="hello"

S = "hello"
vowels = 0
con = 0
 
for ch in S :
  if ch in ("a","e","i","u","o"):
     vowels = vowels+1

  else:
     con = con+1


print ("vowels ",vowels)
print ("cont",con)           


