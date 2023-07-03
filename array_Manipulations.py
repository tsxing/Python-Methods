#sum of absolute value of array elements
sum = sum(abs(element) for element in arr) 

#count number of consecutive negative numbers in array (includes singular negative numbers)
temp = False  
for i in arr:
  if i<0 and not temp: 
    temp = True 
    cnt += 1
  if i>0:
    temp = False 
