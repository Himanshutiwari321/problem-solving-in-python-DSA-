# print name n times ----- recursion problem 
n = 10

def func(count):

  if count == n:
    return 
  func(count+1)
  print(count)
  
func(0)  


