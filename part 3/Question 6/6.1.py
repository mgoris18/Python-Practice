#hint: modulo (%) and floored division (//) may be used
#solution accepts an 8-digit integer representing an unformatted product code
#solution outputs formatted product code as a string in the format XX-XXX-XXX

productCode = int(input())

last3 = productCode % 1000

remaining = productCode // 1000

middle3 = remaining % 1000

first2= remaining // 1000

print(f'{first2:02d}-{middle3:03d}-{last3:03d}')