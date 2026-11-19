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
import math


first_name = input()
last_name = input()
item = input()
price_text = input()
qty = int(input())
customer_type = input()
payment = float(input())
subtotal = float(input())

if customer_type.strip().upper() == "STUDENT":
    discount = subtotal * 0.10
elif customer_type.strip().upper() == "SENIOR" or customer_type.strip().upper() == "PWD":
    discount = subtotal * 0.20
else:
    discount = 0

if subtotal >= 500:
    discount += 25

print(f"Customer: {first_name.strip().title()}, {last_name.strip().title()}")
print(f"Item: {item.strip().title()} x{qty}")
print(f"Subtotal: {float(price_text.replace('P', '').replace(',', '')) * qty:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT (12%): {float(price_text.replace('P', '').replace(',', '')) * qty * 0.12:.2f}")
print(f"Total: {float(price_text.replace('P', '').replace(',', '')) * qty * 1.12:.2f}")
print(f"Paid: {payment:.2f}")
print(f"Change: {payment - (float(price_text.replace('P', '').replace(',', '')) * qty):.2f} pesos and {(payment - (float(price_text.replace('P', '').replace(',', ''))) * qty):.2f} centavos")