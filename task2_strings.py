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
# RULE: never put text inside input(). The grader t ypes the answers for you.

first_name = input().strip()
last_name = input().strip()
item = input().strip()
qty = input().strip()
student_id = input().strip()

print(f"Customer: {first_name} {last_name}")
print(f"Initials: {first_name[0].upper()}{last_name[0].upper()}")
print(f"Item:  {item} {qty}")
print(f"Id: { "*" * 5}{student_id[-3:]}")

