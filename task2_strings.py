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
first_name = "Joey Mark"
Last_Name = "Pelongco"
Item = "Shampoo"
qty = 4
Student_Id = "150764"

first_clean = first_name.upper().title()
last_clean = last_name.upper().title()
item_clean = item.upper().title()
qty_clean = qty.upper().title()
Customer = first_name + " " + last_name
Initials = first_name[0] + last_name [-3:]
first_name.len()
Item = item + " " + qty 

print(f"Customer : {Customer.title()}")
print(f"Initials : {Initials.title()}")
print(f"Item {Item.title()}")
print(f"Student_ID : {Student_Id}")