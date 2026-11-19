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

f_name = first_name.strip().title()
l_name = last_name.strip().title()
item_name = item.strip().title()

price = float(price_text.replace("P","").replace(",",""))
subtotal = round(price * quantity, 2)
vat = round(subtotal * 0.12, 2)
total = round(subtotal + vat, 2) 
change = round(payment - total, 2)

change_centavos = int(round(change * 100))
pesos = change_centavos // 100
centavos = change_centavos % 100

if subtotal >= 500 and customer_type == Student:
    discount = (subtotal * .12) - 25
elif subtotal >= 500 and customer_type == senior or pwd:
    discount = (subtotal * .20) - 25
elif subtotal  >= 500:
    discount = subtotal - 25
else:
    discount = subtotal

    if payment == subtotal:
        payment = "Payment OK"
    else:
        payment = "Insufficient Balance"

print(f"Customer: {f_name} {l_name}")
print(f"Item: {item_name} x {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"VAT (12%): {vat:.2f}")
print(f"Total: {total:.2f}")
print(f"Paid: {payment}")
print(f"Change: {pesos} pesos and {centavos} centavos")
print("Discount:", discount)
print("Payable:", subtotal - discount)
print("payment", payment)

