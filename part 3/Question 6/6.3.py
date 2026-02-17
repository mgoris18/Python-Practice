#hint: modulo (%) and floored division (//) may be used
#solution accepts a 12-digit integer representing an unformatted serial number
#solution outputs formatted serial number as a string in the format XXXX-XXXX-XXXX

number = int(input())

first4 = number // 100000000

remaining = number % 100000000

middle4 = remaining // 10000

last4 = remaining % 1000

print(f"{first4:04d}-{middle4:04d}-{last4:04d}")