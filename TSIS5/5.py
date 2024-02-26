import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
def match_a_followed_by_b(content):
    pattern = re.compile(r'а.*б$')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("A sequence of a single uppercase letter followed by lowercase letters:")
        for line in lines:
            print(line)
    else:
        print("string is not")

match_a_followed_by_b(content)
