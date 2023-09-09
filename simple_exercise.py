weight = input("Weight: ")

unit = input("(K)g or (L)bs: ")
 
if unit.upper() == "K":
    converted = float(weight) / 0.45
    print(f"Weight in Lbs is: {converted}")
else:
    converted = float(weight) * 0.45
    print(f"Weight in Kg is: {converted}")