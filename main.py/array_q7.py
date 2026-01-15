# all factors for given number.

n = [1,2,3,4,5,6,7,8,9,10]
num = len(n)
k = 10
total = []

for i in range (1,num//2+1): # this is range (0 - n-1 ) tak chalti hai isi liye hme +1 lagana padta hai last element ko get karne ke liye,,,,,,, // hme (.) ke bad ka element nhi deta 
    if k%i == 0:
      total.append(i)
total.append(k)
    
print (total)     


      
    
           
        
         
