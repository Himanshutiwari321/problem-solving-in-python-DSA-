# string  are pallidrom or not  using 

s = "madam"
rev = ""

for i in range(len(s)-1,-1,-1):
  
    rev = rev + s[i]

if s==rev:
    print("palidrom")
else:
    print("not palidrom")

#time compexcity = o(n)
# space complexcity = o(n)    





# 2 - pointer aporoch for cheking palidrom or not 
str = "madaa"

left = 0
right = len(str)-1

while left < right:
   if str[left] != str[right]:
      print ("not palidrom")
      break
   left+=1
   right-=1
else:
    print("palidrom")  

#time compexcity = o(n)
# space complexcity = o(1)         