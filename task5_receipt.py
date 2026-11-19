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
first_name = first_name.strip()
last_name = last_name.strip()
fullname = first_name + " " + last_name
item = item.strip()
price_text = price_text.strip()
price_text = price_text.replace("P", "")
price_text = price_text.replace(",", "")
price = float(price_text)
subtotal = round(price * qty, 2)
customer_type = customer_type.strip().lower()
if customer_type == "Student":
    discount = subtotal * 0.10
elif customer_type == "Senior" or customer_type == "PWD":
    discount = subtotal * 0.20
else:
    discount = 0
if subtotal >= 500:
    discount = discount + 25
discount = round(discount, 2)
Vat = round((subtotal - discount) * 0.12, 2)
Total = round((subtotal - discount) + Vat, 2)
print("Customer:", fullname.title())
print("Item:", item.title() + " x" + str(qty))
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT (12%): {Vat:.2f}")
print(f"Total: {Total:.2f}")
if payment >= Total:
    Change = round(payment - Total, 2)
    cent = int(round(Change * 100))
    pesos = cent // 100
    centavos = cent % 100
    print(f"Paid: {payment:.2f}")
    print(f"Change: {pesos} pesos and {centavos} centavos")
else:
    print("Insufficient payment")