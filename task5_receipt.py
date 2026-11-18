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

price_text_convert = float(price_text[1:].replace(',', ''))
subtotal = price_text_convert * qty
vat = subtotal * 0.12
total = subtotal + vat
change = payment - total

STUDENT_DISCOUNT = 0.10
SENIOR_PWD_DISCOUNT = 0.20
OTHER_DISCOUNT = 0.00

if customer_type.strip() == "SENIOR" or customer_type.strip() == "PWD":
    discount = subtotal * SENIOR_PWD_DISCOUNT
elif customer_type.strip() == "STUDENT":
    discount = subtotal * STUDENT_DISCOUNT
else:
    discount = subtotal * OTHER_DISCOUNT

if subtotal >= 500:
    discount += 25

print("Customer: " + first_name.title() + " " + last_name.title())
print(f"Item: {item.title()} x{qty}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT (12%): {vat:.2f}")
print(f"Total: {total:.2f}")
print(f"Paid: {payment:.2f}")
print(f"Change: {int(change)} pesos and {int((change * 100) // change % 100)} centavos")
