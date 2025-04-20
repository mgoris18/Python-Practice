temperatures = [67, 72, 78, 69, 74]

given_temp = int(input())

temp_min = min(temperatures)
temp_max = max(temperatures)

temp_between_min_max = temp_min < given_temp < temp_max

print("Within Range?", temp_between_min_max)