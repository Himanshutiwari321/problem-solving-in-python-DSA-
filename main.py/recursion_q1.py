#print x ,N times . given x=15 and n=4

def func(x,N):
  if N==0:
    return
  print(x)
  func(x,N-1) 


func(15,4)  

#print 1 to N , given N=5
def fun (i,N):
  if i>N:
    return 
  print(i)
  fun(i+1,N)

fun(1,5)  
 


