data = [100, 3.14, "WGU", {"CS": "Python"}, [1,2,3], (5,6)]
descriptions = ["Whole number", "Decimal number", "Text", "Dictionary", "List", "Tuple"]

index = int(input())

element_one = data[index]

element_two = descriptions[index]

element_one_type = type(element_one)

element_one_name = element_one_type.__name__


print(f"{element_two} -> {element_one_name}")