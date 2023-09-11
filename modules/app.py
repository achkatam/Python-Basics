import converters
import utils

# see the difference between the two imports
from converters import kg_to_lbs

# result = converters.kg_to_lbs(100)

# print(converters.kg_to_lbs(70))

# print(result)

numbers = [10, 3, 6, 2, 22]
result = utils.find_max(numbers)
print(result)
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(len(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(utils.average(numbers))