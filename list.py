# Create list
nums = [5, 2, 9, 1]

# Add elements
nums.append(7)            # Add to end
nums.insert(2, 3)         # Insert at index
nums.extend([10, 11])     # Add multiple elements

# Remove elements
nums.remove(2)            # Remove first occurrence of 2
val = nums.pop(1)         # Remove by index, returns value
del nums[0]               # Delete by index

# Check and count
print("Index of 9:", nums.index(9))  # Find index
print("Count of 1:", nums.count(1))  # Count occurrence

# Sort & reverse
nums.sort()               # Sort ascending
nums.reverse()            # Reverse order

# Copy & clear
copy_nums = nums.copy()   # Make a copy
nums.clear()              # Remove all elements

# Built-in functions
print("Length:", len(copy_nums))
print("Max:", max(copy_nums))
print("Min:", min(copy_nums))
print("Sum:", sum(copy_nums))

# Slicing
print("Sliced:", copy_nums[1:4])
