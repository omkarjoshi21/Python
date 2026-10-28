#Looping Statements

#continue
print("Output for continue statement")
for i in range(5):  
    if i == 2:
        continue
    print(i)

#break
print("Output for break statement")
for i in range(5):
    if i == 3:
        break
    print(i)

#Loop Else
print("Output for loop else statement")
for i in range(3):
    print(i)
else:
    print("Loop completed successfully")    


