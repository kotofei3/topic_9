letter: str = input()
text_cget: str = ""
text_no_get: str = ""

for i in range(len(letter)):
    item = letter[i]
    if ord(item) % 2 == 0:
        text_no_get += item
    else:
        text_cget += item

print(text_cget)
print(text_no_get)
