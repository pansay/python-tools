vat_regular = 7.7 / 100
vat_reduced = 2.5 / 100

amount_regular = int(input('Amount of purchases at regular rate:'))
amount_reduced = int(input('Amount of purchases at reduced rate:'))

due_amount = (amount_regular * vat_regular) + (amount_reduced * vat_reduced)

print('Due amount:', due_amount)
