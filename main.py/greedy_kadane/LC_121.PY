#best time to buy and sell stocks 
prices = [7,1,5,3,6,4]

left = 0
max_profit = 0

for right in range (1,len(prices)):
    if prices[left] > prices[right]:
          left=right
    else:
       profit  = prices[right] - prices[left]
       max_profit =max(max_profit , profit)   
print(max_profit)