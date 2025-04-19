#Covert total minutes into hours and minutes
#accept total minutes input
totalMinutes = int(input())

#60 minutes in an hour
hours = totalMinutes // 60 

minutes = totalMinutes % 60

print("Hours:", hours)
print("Minutes:", minutes)