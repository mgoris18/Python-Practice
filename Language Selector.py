languages = ["Python", "JavaScript", "C++", "Go", "Rust", "Swift"]

language_index = int(input())

try:
    languages_selector = languages[language_index]
    print(languages_selector)
except(IndexError):
    print("Selection error")