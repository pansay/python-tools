#
#    we want to show in e.g. M if there is at least 1 M, that is, optimal so that
#        number/(1000^optimalExp) >= 1
#    mathematics->logarithms->
#        optimalExp = log(number) / log(1000);
#

import math

units = ['','k','M','G','T','P','E','Z','Y']

def formatNumber (number, decimals = 2) :
  optimalExp = math.floor( math.log(number) / math.log(1000) )
  number = number / (1000 ** optimalExp)
  return str(round(number, decimals)) + units[optimalExp]

inputNumber = int(input('number: '))
print(formatNumber(inputNumber))
