#Write a program that takes an integer inout representing a total number of seconds and converts it to days, hours, minutes, and remaining seconds
#accept total seconds as an input

total_seconds = int(input())

#(24 * 60) * 60 to find seconds in a day
#86400

days = total_seconds // 86400

left_over_seconds = total_seconds % 86400

#60*60 to find seconds in hour
#3600
hours = left_over_seconds // 3600
left_over_seconds = left_over_seconds % 3600

#60 seconds in a minute
minutes = left_over_seconds // 60
left_over_seconds = left_over_seconds % 60

remaining_seconds = left_over_seconds // 1


print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)

