# sum of 1 to N

def fun (sum, i,N):
   if i>N:
      print(sum)
      return 
   fun(sum+i,i+1,N)
   
fun(0,1,5) # sum,i,N


#sum of 1 to N but different logic 
def func(N):
   if N==1:
      return 1
   return N+func(N-1)

result=func(5)   
print(result)   
