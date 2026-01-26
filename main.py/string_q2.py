# tring are pallidrom or not 

s = "madam"
rev = ""

for i in range(len(s)-1,-1,-1):
  
    rev = rev + s[i]

if s==rev:
    print("palidrom")
else:
    print("not palidrom")

      