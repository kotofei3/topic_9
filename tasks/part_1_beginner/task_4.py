text: str = "Python"
if text:
    number = []
    i = 0
    while i < len(text):
        line = text[i]

        if line.isdigit():
            number.append(line)

        i += 1

    for j in number:
        print(j + "₽ ", end='')


if not number:
    print(False)
