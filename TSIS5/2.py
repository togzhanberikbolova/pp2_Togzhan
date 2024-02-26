import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
def find_a_followed_by_2_to_3_bs(content):
    pattern = re.compile(r'а{1}б{2,3}')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("lines that are followed by two or three b:")
        for line in lines:
            print(line)
    else:
        print("string is not")

find_a_followed_by_2_to_3_bs(content)