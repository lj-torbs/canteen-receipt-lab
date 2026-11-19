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

first_name = ("Juliana")
last_name =("Mendez")
item =("Rice Meal")
qty =(2)
student_id =(0000152069)



print(f"Customer: {first_name} {last_name}".strip().title())
print(f"Initials: {first_name[0]}.{last_name[0]}.".upper()) 
print(f"Item: {item}".title()(f"x{qty}.".lower()))
print(f"id: {student_id}", "*" * 6 + student_id[-3:])


# TODO: write your code below   

