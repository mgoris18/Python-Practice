tempinF = int(input())

#Classify tempinF
#Below 32°F: Freezing
#Between 32°F and 60°F (inclusive): Cold
#Between 61°F and 85°F (inclusive): Warm
#Above 85°F: Hot

#If the input is below -100°F, return: "Temperature too low"
#If the input is above 150°F, return: "Temperature too high"
if tempinF < -100:
    print("Temperature too low")
elif tempinF > 150:
    print("Temperature too high")
elif tempinF < 32:
    print("Freezing")
elif tempinF >= 32 and tempinF <= 60:
    print("Cold")
elif tempinF >= 61 and tempinF <= 85:
    print("Warm")
elif tempinF > 85:
    print("Hot")



