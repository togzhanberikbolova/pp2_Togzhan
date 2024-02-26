import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
def find_a_followed_by_bs(content):
    pattern = re.compile(r'а+б*')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("Strings followed by a zero or more b:")
        for line in lines:
            print(line)
    else:
        print("string is not")

find_a_followed_by_bs(content)