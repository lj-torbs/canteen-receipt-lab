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

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
item = input("Enter item name: ")
qty = int(input("Quatity of an item: "))
student_id = int(input("Student ID: "))

# TODO: write your code below
print()
print(f"Customer: {first_name} {last_name}")
print(f"Initials: {str.upper(first_name)[0]}.{str.upper(last_name)[0]}.")
print(f"Item: {item} x{qty}")
print(f"ID: {student_id}")
