# Python Complete Learning - From Basics to Lists and Dictionaries
# Author: Sagar M Ganiger
# Date: February 23, 2026
# Topics: Variables, Data Types, Strings, Lists, Tuples, Sets, Dictionaries

print("=== PYTHON BASICS ===")

# 1. VARIABLES AND DATA TYPES
name = "Sagar"  # String
age = 20  # Integer
height = 5.8  # Float
is_student = True  # Boolean

print(f"Name: {name}, Age: {age}, Height: {height}")
print(f"Is Student: {is_student}")

# 2. STRINGS
greeting = "Hello from Hubballi"
print(greeting.upper())
print(greeting.lower())
print(greeting.split())
print(len(greeting))

# String slicing
print(greeting[0:5])  # Hello
print(greeting[-8:])  # Hubballi

# 3. NUMBERS AND OPERATIONS
x = 10
y = 3
print(f"Add: {x + y}, Subtract: {x - y}")
print(f"Multiply: {x * y}, Divide: {x / y}")
print(f"Floor Div: {x // y}, Modulo: {x % y}")
print(f"Power: {x ** y}")

# 4. LISTS (ARRAYS IN PYTHON)
print("\n=== LISTS ===")
fruits = ["apple", "banana", "orange", "mango"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# List methods
fruits.append("grape")
print("After append:", fruits)

fruits.insert(1, "watermelon")
print("After insert:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

popped = fruits.pop()
print(f"Popped: {popped}, List: {fruits}")

# List slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First 5:", numbers[:5])
print("Last 5:", numbers[-5:])
print("Every 2nd:", numbers[::2])

# List comprehension
squares = [n**2 for n in range(1, 6)]
print("Squares:", squares)

# 5. TUPLES (Immutable lists)
print("\n=== TUPLES ===")
coordinates = (10, 20)
print("Coordinates:", coordinates)
print("X:", coordinates[0], "Y:", coordinates[1])

# 6. SETS (Unique elements)
print("\n=== SETS ===")
unique_nums = {1, 2, 3, 3, 4, 5, 5}
print("Set:", unique_nums)  # Duplicates removed

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# 7. DICTIONARIES (Key-Value Pairs)
print("\n=== DICTIONARIES ===")
student = {
    "name": "Sagar",
    "age": 20,
    "city": "Hubballi",
    "college": "KLE Tech",
    "course": "Engineering"
}

print("Student:", student)
print("Name:", student["name"])
print("College:", student.get("college"))

# Adding/updating
student["year"] = 2
student["branch"] = "Computer Science"
print("Updated:", student)

# Dictionary methods
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Checking keys
if "name" in student:
    print("Name exists!")

# Removing items
student.pop("year")
print("After pop:", student)

# Nested dictionary
courses = {
    "python": {"instructor": "Dr. Smith", "duration": "3 months"},
    "java": {"instructor": "Prof. Kumar", "duration": "4 months"}
}
print("\nCourses:", courses)
print("Python instructor:", courses["python"]["instructor"])

# Dictionary comprehension
square_dict = {x: x**2 for x in range(1, 6)}
print("Square dict:", square_dict)

print("\n=== LEARNING COMPLETE ===")
