filename = input()

with open(filename, "r") as file:
    words = file.read().splitlines()

sentence = " ".join(words)
reversed_sentence = sentence[::-1]

with open(filename, "a") as file:
    file.write("\n" + reversed_sentence)

with open(filename, "r") as file:
    print(file.read())