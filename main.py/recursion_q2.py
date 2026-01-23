# N to 1 using tail recurison 
def fun (i,N):
  if i>N:
    return 
  fun(i+1,N)
  print(i)

fun(1,5)  

#N to 1 using head recursion 

def func(N):
  if N==0:
    return 
  print(N)
  func(N-1)

func(5)  