a, b, c, d, p = map(int, open(0))

a_price = p * a
if p <= c:
    y_price = b
else:
    y_price = b + (p-c) * d

print(min([a_price, y_price]))