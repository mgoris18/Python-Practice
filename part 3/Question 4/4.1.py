#solution accepts three integer values representing length, width, and height of a rectangular prism
#solution outputs the rectangular prism volume in cubic meters using formula V = l * w * h

length = int(input())
width = int(input())
height = int(input())

volume = length * height * width

print(f"Rectangular prism volume: {float(volume)} cubic meters")