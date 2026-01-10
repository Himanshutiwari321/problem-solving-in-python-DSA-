# character freqency in a string 

str = "helloo"
freqency = {}

for ch in str :
  if ch in freqency:
    freqency[ch]= freqency[ch]+1

  else:
    freqency[ch]= 1 

print(freqency)     