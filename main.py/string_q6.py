string  = "swiss"
unique = {}
for ch in string :
  if ch in unique:

    unique[ch] = unique[ch] + 1
  else:
    unique[ch] = 1


for ch in string:
    if unique[ch] == 1:
      

      break    

if unique[ch] != 1:
   print ("not found unique character ")  
else:
  print ("unique character", ch)  
  

  