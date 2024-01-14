# line = "     Yandex"
#
# i = 0
# while i < len(line):
#     text = line[:i + 1]
#     print(text)
#     i += 1

line = input()
is_printed = False
text = ""

for char in line:
    if is_printed or char != " ":
        text += char
        print(text)
        is_printed = True
