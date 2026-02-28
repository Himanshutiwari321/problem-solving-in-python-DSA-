#First negative in every window of size k


from collections import deque

nums = [12,-1,-7,8,-15,30,16,28]
k = 3 

n = len(nums)
left = 0
right = 0
result = deque()
q = []

while right< n:
    if nums[right]<0:
      result.append(nums[right])
    if right - left +1 < k:
      right+=1

    elif right - left +1 == k:
        if len(result) == 0:
            q.append(0)
          

        else:
            q.append(result[0])
            if result[0]==nums[left]: 
                result.popleft()             
        left+=1
        right+=1

print(q)     

##---2-- this code print total number of window at least one nagative number 


# nums = [12,-1,-7,8,-15,30,16,28]
# k = 3 

# n = len(nums)
# left = 0
# right = 0
# result = deque()
# q = 0

# while right< n:
#     if nums[right]<0:
#       result.append(nums[right])
#     if right - left +1 < k:
#       right+=1

#     elif right - left +1 == k:
#         if len(result) == 0:
#           q+=0

#         else:
#           q+=1
#           if result[0]== nums[left]:
#              result.popleft()             
#         left+=1
#         right+=1

# print(q) 




##--- 3 -----this code print total number of window  size of k 

# nums = [12,-1,-7,8,-15,30,16,28]
# k = 3 

# n = len(nums)
# left = 0
# right = 0
# result = deque()
# q = 0

# while right< n:
#     if nums[right]<0:
#       result.append(nums[right])
#     if right - left +1 < k:
#       right+=1

#     elif right - left +1 == k:
#         if len(result) != 0:
#           q+=1

#         left+=1
#         right+=1

# print(q) 