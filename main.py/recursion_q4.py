#factoril question 

def fect(N):
  if N==1:
    return 1
  return N * fect(N-1)

result = fect(6)
print(result)