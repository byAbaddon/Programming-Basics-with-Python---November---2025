age, gender = float(input()), input()

if gender == "f":
    print("Miss" if age < 16 else "Ms.")
else:
    print("Master" if age < 16 else "Mr.")

