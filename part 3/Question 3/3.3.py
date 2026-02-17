data = [1, 2.5, "hello", (4, 5), {"a": 1}, True]

index = int(input())

data_type = type(data[index]).__name__

print(f"Element {index}: {data_type}")