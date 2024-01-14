text:str = "hello"
symbol:str = "l"

if symbol in text:
    for i in range(len(text)):

        if text[i] == symbol:
            print(i)
            break
else:
    print(-1)






