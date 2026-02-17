#hint: modulo (%) and floored division (//) may be used
#solution accepts a 10-digit integer representing an unformatted phone number
#solution outputs formatted phone number as a string in the format (XXX) XXX-XXXX

number = int(input())

first3 = number // 10000000

remaining = number % 10000000

middle3 = remaining // 10000

last4 = remaining % 10000

print(f"({first3:03d}) {middle3:03d}-{last4:04d}")