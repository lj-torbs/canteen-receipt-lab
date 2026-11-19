# Task 5: Put it all together (15 points)
#
# Combine your work from tasks 2, 3 and 4 into one receipt program. Copy and paste
# the parts you need from your own earlier files.
#
# The first seven lines read the input for you. Do not change them.
# Example, if the input is "  juan ", " CRUZ", burger, P100, 2, student and 300,
# the program must print EXACTLY these lines:
#
#     Customer: Juan Cruz
#     Item: Burger x2
#     Subtotal: 200.00
#     Discount: 20.00
#     VAT (12%): 21.60
#     Total: 201.60
#     Paid: 300.00
#     Change: 98 pesos and 40 centavos
#
# Notes:
#   Subtotal and discount work as in tasks 3 and 4.
#   VAT is 12% of the amount AFTER the discount.
#   Total = (subtotal - discount) + VAT, all rounded to 2 decimals.
#   If the payment is not enough, the last two lines are replaced by one line:
#       Insufficient payment
#
# RULE: never put text inside input(). The grader types the answers for you.

first_name = input()
last_name = input()
item = input()
price_text = input()
qty = int(input())
customer_type = input()
payment = float(input())

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

price_text = input()
qty = int(input())
payment = float(input())

price = float(price_text.replace("P", "").replace(",", ""))

subtotal = round(price * qty, 2)
vat = round(subtotal * 0.12, 2)
total = round(subtotal + vat, 2)
change = round(payment - total, 2)

total_centavos = int(round(change * 100))
pesos = total_centavos // 100
centavos = total_centavos % 100

print(f"Subtotal: {subtotal:.2f}")
print(f"VAT (12%): {vat:.2f}")
print(f"Total: {total:.2f}")
print(f"Paid: {payment:.2f}")
print(f"Change: {pesos} pesos and {centavos} centavos")

customer_type = input()
subtotal = float(input())
payment = float(input())

cleaned_type = customer_type.strip().lower()

if cleaned_type == "student":
    pct_discount = subtotal * 0.10
elif cleaned_type in ("senior", "pwd"):
    pct_discount = subtotal * 0.20
else:
    pct_discount = 0.0

extra_discount = 25.0 if subtotal >= 500 else 0.0

discount = round(pct_discount + extra_discount, 2)
payable = round(subtotal - discount, 2)

print(f"Discount: {discount:.2f}")
print(f"Payable: {payable:.2f}")
if payment >= payable:
    print("Payment OK")
else:
    print("Insufficient payment")