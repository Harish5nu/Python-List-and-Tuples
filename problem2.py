# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple

# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Removing elements
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# Length of the list
print(len(fruits))  # Output: 3