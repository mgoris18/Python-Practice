#Month: 04  
#Day: 18  
#Year: 2025
#input mmddyyyy

unformatted_date = int(input())

unformatted_date_string = str(unformatted_date).zfill(8)

month = unformatted_date_string[0:2]
day = unformatted_date_string[2:4]
year = unformatted_date_string[4:8]

print("Month:", month)
print("Day:", day)
print("Year:", year)
