#best time to buy and sell stocks 

#brute fource solution o(n2)
prices = [7,1,5,3,6,4]

profit = 0

for i in range (len(prices)):
    for j in range (i+1,len(prices)):
        curr_profit = prices[j] - prices[i]
        if curr_profit > profit :
            profit = curr_profit

print(profit)            



#optimize solution o(n)
prices = [7,1,5,3,6,4]

min_price = prices[0]
profit = 0

for i in range (len(prices)):
    curr_price = prices[i]- min_price
    if curr_price>profit:
       profit = curr_price
    
    min_price = min(min_price , prices[i])   
print(profit)