#solution accepts four integer inputs
#solution outputs three products of input values; convert before calculating product
#first output: product maintained as integer values
#second output: product converted to float values
#third output: product converted to string values (concatenate)

a = int(input())
b = int(input())
c = int(input())
d = int(input())

integer = a * b * c * d

float_sum = float(a) * float(b) * float(c) * float(d)

string_sum = str(a) + str(b) + str(c) + str(d)

print(f"Integer: {integer}")
print(f"Float: {float_sum}")
print(f"String: {string_sum}")