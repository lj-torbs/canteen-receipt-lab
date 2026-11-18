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

first_name = input().strip()
last_name = input().strip()
item = input().strip()
qty = input().strip()
student_id = input().strip()


full_name = f"{first_name.title()} {last_name.title()}"
initials = f"{first_name[0].upper()}.{last_name[0].upper()}."
masked_id = "*" * (len(student_id) - 3) + student_id[-3:]

print(f"Customer: {full_name}")
print(f"Initials: {initials}")
print(f"Item: {item.title()} x{qty}")
print(f"ID: {masked_id}")

