phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

result = " "
for ch in phone: 
    result += f"{digits_mapping.get(ch, '!')} "
    
print(result)