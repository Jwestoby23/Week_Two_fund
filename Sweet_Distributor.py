sweet = input("How many sweets do you have; ")
sweet = int(sweet)

pupils = input("How many pupils attended today; ")
pupils = int(pupils)

print("Each student will have", sweet // pupils, "sweets")
print("You will have",sweet % pupils, "left over")