# it is string question but most of the person mistake on this , because inside the string have integer so that's a confussion when someone will look. 

n = "12654"
num = n 
rev  = ""

for i in range(len(num)-1,-1,-1):
  rev = rev + num[i]
print (rev)


# you can check it is palidrome or not using if else condition 