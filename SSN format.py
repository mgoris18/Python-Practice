

unformatted_number = int(input())

unformatted_number_string = str(unformatted_number)

part_one = unformatted_number_string[0:3]
part_two = unformatted_number_string[3:5]
part_three = unformatted_number_string[5:9]

print(f'{part_one}-{part_two}-{part_three}')