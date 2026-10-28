# 08-10-2026

# Assignment - Create a list of 10 numbers and display the sum of last 4 elements.
# Assignment - Remove the items from the list located at 2nd and 5th position and display the new list.
# Assignment - Print the difference of highest and lowest number in the list. 
# Assignment - Append a new element in a list which is half of the item of third position in the list 

# Practice Questions on string -

# 1. Print sum of first 10 even numbers
# 2. Accept two values S and N, Print square of first N numbers starting from S
# 3. Reverse the accepted string and print it
# 4. Accept a sentence from user and count the vowels
# 5. Reverse the list


#09-10-2026
#Practice Assignments

# 1 to 10 odd numbers
print("Odd Numbers from 1 to 10 are : ")
for i in range(1, 11):  
    if i % 2 != 0:
        print(i) 

# Create heterogeneous list of numbers and names. Split the list from highest number.
list1 = [1, 2, 3, "Omkar", 6, "Joshi", 4, 5]
a=0
for i in list1:
    if type(i)==int:
        if i>a:
            a=i
    
    
    
        
# Accept the name and check if its palindrome or not.
name=input("Enter a name: ")
start=0
end=len(name)-1


# Print the sum of digits.
a=-65442
sum=0
while(a>0):
    b=a%10
    sum=sum+b
    a=a//10
print(sum)      

# Print following pattern 
#*  
#* *
#* * *
for i in range(1,4):
    for j in range(i):
        print("*", end="")
    print()