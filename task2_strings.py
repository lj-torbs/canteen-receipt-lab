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

first_name = first_name.strip().title()
qty = qty.strip()
item = item.strip()
print(f"Costumer:", first_name, last_name, )
print("Initials:",first_name[-4],".",last_name[-4].upper(),".",)
print("Item:", item, (qty))
print("ID: ", student_id, student_id.strip())
