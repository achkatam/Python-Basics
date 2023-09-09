numbers = [1,2,3,4,5]
print(numbers)

# Append at the end of the list
numbers.append(6)
print(numbers)

# Insert at a specific index [index, value]
numbers.insert(3, 0)
print(numbers)

# Removing elements
numbers.remove(3)
print(numbers)

# Remove the last element like stack in C#
numbers.pop()
print(numbers)

# Remove element at a specific index
numbers.pop(2)
print(numbers)

# boolean in list
boolean = 1 in numbers
print(boolean)

# Elements count in list
print(len(numbers))
  
# Index of an element
print(numbers.index(4))

# Reverse sorting
numbers.reverse()
print(numbers)

# Sorting elements
numbers.sort()
print(numbers)

# Copying a list
numbers2 = numbers.copy()
print(numbers2)

# Remove all elements
numbers.clear()
print(numbers)