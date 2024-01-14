# 1 -------------variant
# n = input()
# text = ""
# for i in range(len(n)):
#
#     if n[i] not in text:
#         text += n[i]
# print(text)


# 2 ---------variant
# leter: str = "DuckDuckGo"
# text: str = ""
#
# i: int = 0
# while i < len(leter):
#
#     if leter[i] not in text:
#         text += leter[i]
#     i += 1
# print(text)


leter: str = "DuckDuckGo"
text: list = []

count: int = 0
i: int = 0
while i < len(leter):
    count += 1

    if leter[i] not in text:
        n = text.append(leter[i])

    i += 1

j:int = 0
while j < len(text):
    t = text[j]
    print(t, end='')

    j += 1
