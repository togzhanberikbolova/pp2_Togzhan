import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
def find_upper_case_letter_followed_by_lower(content):
    pattern = re.compile(r'\b[A-Z]{1}[a-z]+\b') # r'\b[А-Я]{1}+[а-я]+\b'
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("A sequence of a single uppercase letter followed by lowercase letters:")
        for line in lines:
            print(line)
    else:
        print("string is not")

find_upper_case_letter_followed_by_lower(content)