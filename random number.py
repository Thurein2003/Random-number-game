import random
ans = random.randint(0,20)
for x in range(0,3):
   
    global i
    i =int(input("enter a number"))
    if i<ans :
        print ( "your answer is less than ans")
    elif i>ans:
        print ( "your answer is greater than ans")
    elif i == ans:
        print ( "your answer is correct")
print ("the answer is :",ans)