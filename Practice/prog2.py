# Creating a dictionary
student = {"name": "Omkar", "age": 22, "course": "MCA"}

# 1. Accessing values using keys
print("Name:", student["name"])
print("Course:", student.get("course"))  # Another safe way to get values

# 2. Adding a new key-value pair
student["city"] = "Pune"
print("After adding city:", student)

# 3. Updating an existing value
student["age"] = 23
print("After updating age:", student)

# 4. Deleting a key-value pair
del student["course"]
print("After deleting course:", student)

# 5. Checking if a key exists
print("Is 'name' in dictionary?", "name" in student)

# 6. Looping through all keys and values
print("\nFinal Dictionary Items:")
for key, value in student.items():
  print(key, "->", value)