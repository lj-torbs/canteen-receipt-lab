# Task 2: Strings (15 points)
#
# The first five lines read the input for you. Do not change them.
# Then print exactly four lines. Example, if the input is:
#     "  juan "      (first name)
#     " CRUZ"        (last name)
#     " rice meal "  (item)
#     2              (quantity)
#     2024-1234      (student ID)
# the program prints:
#     Customer: Juan Cruz
#     Initials: J.C.
#     Item: Rice Meal x2
#     ID: ******234
#
# Hints: strip(), title(), upper(), indexing like name[0], slicing like text[-3:],
#        len(), "*" * 5, and f-strings.
#
# RULE: never put text inside input(). The grader types the answers for you.


first_name = input ("First Name: Hannica")
last_name = input ("Last Name: Alzate")
item = input ("item: Rice Meal")
qty = input ("Quantity: x2")
student_id = input ("Id: 151715")


print ("Customer", first_name)
print ("Customer", last_name)
print ("item", item)
print ("Quantity", qty)
print ("Id", student_id)

print(f"Costumer: {first_name} {last_name}".strip().title())
print(f"Initials: {first_name[0].upper()}.{last_name[0].upper()}.")
print(f"Item: {item}".title(), (f"x{qty}".lower()))
print(f"ID: {student_id}".len(), "*" * 5 + student_id[-3:])

#TODO: 