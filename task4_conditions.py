# Task 4: Conditions (25 points)
#
# Discount rules for the canteen:
#     student            -> 10% off the subtotal
#     senior or pwd      -> 20% off the subtotal
#     any other customer -> no percentage discount
# Extra rule: if the subtotal is 500 or more, take an additional 25 pesos off.
# Both rules can apply together (for example a student with a 600 peso order).
#
# The customer type may be typed in any capitalisation and with extra spaces,
# so " SENIOR " counts as senior.
#
# The first three lines read the input for you. Do not change them.
# Print exactly three lines. Example, if the input is student, 200 and 300:
#     Discount: 20.00
#     Payable: 180.00
#     Payment OK
#
# Rules:
#   Discount = percentage discount + the extra 25 if it applies, rounded to 2 decimals
#   Payable  = subtotal - discount, rounded to 2 decimals
#   Last line is "Payment OK" if the payment covers the payable amount
#   (paying the exact amount is OK), otherwise "Insufficient payment".
#
# RULE: never put text inside input(). The grader types the answers for you.

customer_type = input()
subtotal = float(input())
payment = float(input())

# TODO: write your code below
customer_type = customer_type.strip().lower()

if customer_type == "student":
    discount = subtotal * 0.10
elif customer_type == "senior" or customer_type == "pwd":
    discount = subtotal * 0.20
else:
    discount = 0.0

if subtotal >= 500:
    discount += 25.0

discount = round(discount, 2)
payable = round(subtotal - discount, 2)
print(f"Discount: {discount:.2f}")
print(f"Payable: {payable:.2f}")
if payment >= payable:
    print("Payment OK")
else:
        print("Insufficient payment")