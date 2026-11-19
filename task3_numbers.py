# Task 3: Numbers (15 points)
#
# The first three lines read the input for you. Do not change them.
# price_text is typed like P100 or P1,250.50, so you must remove the "P" and any
# commas before converting it to a number.
#
# Print exactly five lines. Example, if the input is P100, 2 and 300:
#     Subtotal: 200.00
#     VAT (12%): 24.00
#     Total: 224.00
#     Paid: 300.00
#     Change: 76 pesos and 0 centavos
#
# Rules:
#   Subtotal = price x quantity, rounded to 2 decimals
#   VAT      = 12% of the subtotal, rounded to 2 decimals
#   Total    = subtotal + VAT, rounded to 2 decimals
#   Change   = payment - total, rounded to 2 decimals. Show it as whole pesos and
#              centavos. Hint: work in centavos first (change x 100), then use // and %.
# Show money with 2 decimals using f"{value:.2f}".
# You may assume the payment is always enough.
#
# RULE: never put text inside input(). The grader types the answers for you.

price_text = input()
qty = int(input())
payment = float(input())

# TODO: write your code below
clean_price = float(price_text.replace("p", "").replace(",", ""))

subtotal =round(clean_price * qty,2)
Vat = round(subtotal * 0.12,2)
Total = round(subtotal + Vat,2)
Change = round(payment - Total,2)

subcentavos = int(round(change * 100))
pesos = (subsentavos // 100)
centavos = round( subsentavos % 100)

print (f"Subtotal: {subtotal:.2f}")
print (f"Vat (12%): {vat:.2f}")
print (f"Total: {Total:.2f}")
print (f"Paid: {payment:.2f}")
print (f"Change: {change} pesos {centavos:.2f} ")