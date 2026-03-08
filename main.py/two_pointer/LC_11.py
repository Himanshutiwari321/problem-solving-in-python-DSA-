#Container with moost water 

height = [1,8,2,6,4,5,8,3,7]

max_water= 0
left = 0
right = len(height)-1
while left<right:
  area = min(height[left], height[right]) * (right - left)
  max_water = max(max_water, area )

  if height[left]<height[right]:
    left+=1
  else:
    right-=1 

print(max_water)
             