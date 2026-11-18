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
print(f"Customer: {first_name.strip().lower().title()} {last_name.strip().lower().title()}")
print(f"Item: {item.strip().lower().title()} x{qty}")
price_text = price_text.strip("P").replace(",", "")
price = float(price_text)
subtotal = round(price * qty, 2)
print(f"Subtotal: {subtotal:.2f}")
customer = customer_type.strip().lower()
discount = 0
if customer == "student":
    discount = round(subtotal * 0.10, 2)
    if subtotal >= 500:
        discount + 25
    payable = round(subtotal - discount, 2)
    VAT = round(payable * 0.12, 2)
    subtotal = (subtotal - discount) + VAT
    print(f"Discount: {discount:.2f}")
    print(f"VAT (12%): {VAT:.2f}")
    print(f"Total: {subtotal:.2f}")
    change = round(payment - payable)
    if change >= 0:
        print(f"Paid: {payment:.2f}")
        change = round((payment - subtotal) * 100, 2)
        print(f"Change: {(change // 100):.0f} pesos and {(change % 100):.0f} centavos")
    else:
        print("Insufficient payment")
elif customer == "senior":
    discount = round(subtotal * 0.20, 2)
    if subtotal >= 500:
        discount + 25
    payable = round(subtotal - discount, 2)
    VAT = round(payable * 0.12, 2)
    subtotal = (subtotal - discount) + VAT
    print(f"Discount: {discount:.2f}")
    print(f"VAT (12%): {VAT:.2f}")
    print(f"Total: {subtotal:.2f}")
    change = round(payment - payable)
    if change >= 0:
        print(f"Paid: {payment:.2f}")
        change = round((payment - subtotal) * 100, 2)
        print(f"Change: {(change // 100):.0f} pesos and {(change % 100):.0f} centavos")
    else:
        print("Insufficient payment")
else:
    if subtotal >= 500:
        discount + 25
    payable = round(subtotal - discount, 2)
    VAT = round(payable * 0.12, 2)
    subtotal = (subtotal - discount) + VAT
    print(f"Discount: {discount:.2f}")
    print(f"VAT (12%): {VAT:.2f}")
    print(f"Total: {payable:.2f}")
    change = round(payment - payable)
    if change >= 0:
        print(f"Paid: {payment:.2f}")
        change = round((payment - subtotal) * 100, 2)
        print(f"Change: {(change // 100):.0f} pesos and {(change % 100):.0f} centavos")
    else:
        print("Insufficient payment")
