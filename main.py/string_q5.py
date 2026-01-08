# check these string are anagram or not .

str1 = "hello"
str2 = "hellt"

if len(str1)!= len(str2):
  print("not anagram")

else:
    if sorted(str1)== sorted(str2):

       print ("anagram")
    else:
       print ("a not an anagram")     