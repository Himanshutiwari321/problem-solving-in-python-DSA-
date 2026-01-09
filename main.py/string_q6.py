string  = "siiss"
unique = ""
for ch in  string :
  if string.count(ch)==1:
    unique = ch
    break

if unique == "":
  print ("not found unique character ")  
else:
  print ("unique character", unique)  
  

  