# Write a program to read a file and count how any vowels are present in its content

f = open("demo.txt", "r")
data = f.read()
count = 0

for i in data:
    if i in "aeiouAEIOU":
        count += 1

print("Total vowels:", count)
f.close()

# Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line

f = open("demo.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))
print("2nd line:", lines[1])
print("4th line:", lines[3])


# Take a sentence from user, split it into words and store them in a list. Print the longest word

sentence = input("Enter a sentence: ")
words = sentence.split()

longest = ""
for w in words:
  if len(w) > len(longest):
    longest = w

print("The longest word is:", longest)


# Read a file, split its content into words, and store them in a list.
   # 1) Print the total number of words
   # 2) Print all unique words

f = open("demo.txt", "r")
data = f.read()
f.close()
words = data.split()
print("Total words:", len(words))
unique = []
for w in words:
  if w not in unique:
    unique.append(w)
print("Unique words:", unique)