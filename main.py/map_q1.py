#hasing question ---- how many time m values in n , count and print ---- it just understand the hashing concept 
n = [1,2,5,5,7,8,7,5,5,10]
m = [1,75,7,5,111,10]



has_map = {}

for i in n:
  if i in has_map:
    has_map[i]+=1

  else:
      has_map[i]=1

for i in m:
    if i in has_map:
       print(i ,"=", has_map[i])



# for strnig 

s = "azyxyyzaaaa"
q = ["d", "a","y","z"]

maap = {}

for i in s:
  if i in maap:
     maap[i] += 1
  else:
      maap[i]= 1

for i in q:
  if i in maap:
    print(i, ":", maap[i])
  else:
      print (i, ": 0") 

        



    
            
