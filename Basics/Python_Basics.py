#This is a Separator Example Program
print("Hello","are you ?", sep=" Who ")

# Python Examples For Commom String Functions

#Sample String
text="  Hello I am Omkar Joshi  "

# 1.Strip spaces from both ends
print("Remove spaces : ",text.strip())

# 2.Convert to Lowercase
print("Lowercase : ",text.lower())  

# 3.Convert to Uppercase
print("Uppercase : ",text.upper())

# 4.Capitalize first letter of each word
print("Capitalize First Letter: ",text.title())

# 5. Title case ( capitalizes each word )
print("Title Case : ",text.title())

# 6. Count occurrences of a substring
print("Letter O occurs : ",text.count("O"), "times")

# 7. Find the position of a substring (-1 if not found)
print("Position of 'Omkar' : ",text.find("Omkar"))

# 8. Replace a substring with another substring
print("Replace 'Omkar' with 'Onkar' : ",text.replace("Omkar", "Onkar"))

# 9. Check if the string starts or ends with certain substring
print("Starts with 'Hello' : ",text.startswith("Hello"))
print("Ends with 'Joshi' : ",text.endswith("Joshi"))

# 10. Split the string list by a delimiter
print("Simple Split : ",text.split())

# 11. Join a list of strings with a separator
words = ["Hello", "I", "am", "Omkar", "Joshi"]
print("Join with space : ", " ".join(words))

# 12. Count the vowels in the string
# Practice this 
vowels = "aeiouAEIOU" 
vowel_count = sum(1 for char in text if char in vowels)
print("Number of vowels : ", vowel_count)

# 13. Using Operators with Strings
txt="Hello"
txt1="Hi"

# Repeat the string 3 times and give a space in between
print("Repeat String : ", (txt + " ") * 3)

# Add two strings together
print("Add two strings : ", (txt + " " + txt1 + " ") * 3)

# 14. Split the string in 2 parts and print
txt3 = input("Enter a string: ")  
print(txt3.find("a"))
print(txt3.replace("a", "B"))

# 15. Sorted list of characters in the string
print("Sorted List of Characters : ", sorted(txt3))

# 16. Take input from user and find alphabetic characters in the string and replace with new



# Functions

#Length
numbers = [1, 2, 3, 4, 5, 7, 5, 9]
print("No. of Items in List are : ", len(numbers))

#Sum
print("Sum of Items in List are : ", sum(numbers))

#Sorting
print("List in ascending order : ", sorted(numbers))
print("List in descending order : ", sorted(numbers, reverse=True))

# Create dictionary

students ={
    101: {"Name": "Aditi", "Scores":[78,85,47]}
}


