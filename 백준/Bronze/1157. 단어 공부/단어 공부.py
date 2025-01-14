word = str(input())

book = {}
for i in word:
    i = i.upper()
    book[i] = book.get(i, 0) + 1

result = [k for k, v in book.items() if v == max(book.values())]
if len(result) >= 2:
    print("?")
else:
    print(result[0])