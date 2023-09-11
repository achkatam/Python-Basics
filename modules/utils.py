def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def average(numbers):
    return sum(numbers) / len(numbers)