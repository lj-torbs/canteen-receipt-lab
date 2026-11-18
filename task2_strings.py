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

first_name = input()
last_name = input()
item = input()
qty = input()
student_id = input()

# TODO: write your code below
print(f"Customer: {first_name.strip().lower().title()} {last_name.strip().lower().title()}")
print(f"Initials: {first_name.strip().lower().title()[0]}. {last_name.strip().lower().title()[0]}.")
print(f"Item: {item.strip().lower().title()} x{qty}")
print(f"ID: {"*" * 6}{student_id[6:]}")


