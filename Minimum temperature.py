temperatures = [65,72,80,68,74]

todays_temp = int(input())

min_temp = min(temperatures)

is_min = todays_temp < min_temp

print("Lower Than Min?", is_min)