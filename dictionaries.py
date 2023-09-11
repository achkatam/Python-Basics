# Defining a dictionary with {}

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["age"])

print(customer.get("age"))
print(customer.get("name"))

customer["name"] = "Jack Smith"
print(customer["name"])

customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])