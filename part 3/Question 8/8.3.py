frameworks = ["React", "Angular", "Vue", "Svelte"]

#use try block with exception "Error" when conversion fails or index is invalid
#solution accepts input
#solution outputs the corresponding string value or "Error"

index = input()

try:
    index = int(index)
    print(frameworks[index])
except:
    print("Error")

