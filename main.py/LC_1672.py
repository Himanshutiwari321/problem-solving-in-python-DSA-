#richest customer wealth

accounts = [[1,2,3],[3,2,1]]

ans =0
for acount in accounts:
   ans = max(ans, sum(acount))
print(ans)   