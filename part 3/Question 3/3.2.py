items = [10, 3.14, False, "cat", [1, 2, 3]]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

index = int(input())
data_type = type(items[index]).__name__

print(f"Element {index}: {data_type}")