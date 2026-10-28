# A sample string
text = "Hello Python Learner"

# 1. Find the length of the string
print("Length:", len(text))

# 2. Change text case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 3. Slicing (getting a piece of the string)
# Extracts characters from index 6 to 11 ('Python')
print("Sliced text:", text[6:12])

# 4. Replace a word inside the string
new_text = text.replace("Learner", "Student")
print("Replaced text:", new_text)

# 5. Check if a word exists in the string
print("Contains 'Python'?", "Python" in text)