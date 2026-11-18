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

price = float(price_text.replace('P', '').replace('p', '').replace(',', ''))

subtotal = round(price * qty, 2)

if customer_type == "student":
    discount = round(subtotal * 0.10)
elif customer_type == "senior" or customer_type == "pwd":
    discount = round(subtotal * 0.20)
else:
    discount = 0.0

    if subtotal >= 500:
        discount += 25.0

discount = round(discount, 2)
after_discount = round(subtotal - discount, 2)
vat = round(after_discount * 0.12, 2)
total = round(after_discount + vat, 2)

print(f"Customer: {first_name} {last_name}")
print(f"Item: {item} x{qty}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT (12%): {vat:.2f}")
print(f"Total: {total:.2f}")

if payment >= total:
    change = round(payment - total, 2)
    change_centavos = round(change * 100)
    change_pesos = change_centavos // 100
    centavos = change_centavos % 100
    print(f"Paid: {payment:.2f}")
    print(f"Change: {change_pesos} pesos and {change_centavos} centavos")

else:
    print("Insufficient payment")

