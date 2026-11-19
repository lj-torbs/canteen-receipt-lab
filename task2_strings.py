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

first_name = input() #first_name = 'juan'
last_name = input() #last_name = 'Cruz'
item = input()  #item = 'rice meal'
qty = input() #qty = '2'
student_id = input() #student_id =  '2024-1234' 

# TODO: write your code below

print("Customer: "+first_name.strip().title() + last_name.strip().title())
print("Initials: "+fist_name[0].title().strip()), (last_name[-3:].title())
print("Item: ", item.title(),"x"qty)
print("ID :" "*" * 5, student_id)
