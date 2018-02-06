# VAT and importing rules see
#  * https://www.estv.admin.ch/estv/fr/home/mehrwertsteuer/fachinformationen/steuersaetze.html
#  * https://www.post.ch/fr/particuliers/index-thematique-pour-les-particuliers/dedouanement-et-dispositions-d-importation/importation-et-reception/prix-du-dedouanement-a-l-importation

# percentages
vat_regular = 7.7 / 100
vat_reduced = 2.5 / 100
customsRate = 3 / 100

# CHF amounts
free_limit = 5
zone1_fee = 11.5
zone2_fee = 16
max_customs_limit = 70

amount_regular = int(input('Amount of purchases at regular rate: '))
amount_reduced = int(input('Amount of purchases at reduced rate: '))
zone = int(input('Type 1 or 2 for Zone 1 (Swiss neighboring countries) or Zone 2 (rest of the world): '))

due_amount = (amount_regular * vat_regular) + (amount_reduced * vat_reduced)

if due_amount < free_limit:
  print('no tax ( VAT total: ', due_amount, ')')
else:
  print('more calc...')


