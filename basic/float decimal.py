import decimal

value=str('6,0865000000e-01')
value2=value.replace(',', '.')
float(value2)
print(value2)

print(decimal.Decimal('5E+3'))
print(decimal.Decimal('5000.00000000'))
