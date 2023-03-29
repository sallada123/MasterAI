import math 
print('How many AutoAuto cars were ordered?')
value=int(input())

# Total volume occupied
result=value*14*9*9

# Ceiling is done to get an integer value
box1=math.ceil(result/(14*10*10)) 
box2=math.ceil(result/(18*18*18))
box3=math.ceil(result/(23*23*18))

# Number of boxes of each size
print('Number of boxes of size 14 x 10 x 10 is',box1)
print('Number of boxes of size 18 x 18 x 18 is',box2)
print('Number of boxes of size 23 x 23 x 18 is',box3)

# Minimize the no. of boxes shipped
if (box1<=box2):
    if (box1<=box3):
       print('The total number of boxes shipped (size = 14 x 10 x 10) is',box1)
elif (box2<=box1):
    if (box2<=box3):
       print('The total number of boxes shipped (size = 18 x 18 x 18) is',box2)
    else:
     print('The total number of boxes shipped (size = 23 x 23 x 18) is',box3)
