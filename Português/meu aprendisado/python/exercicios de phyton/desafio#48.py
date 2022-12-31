v = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        v += 1
        s += c
print(f"""A soma de todos os {v} valores solicitados é {s}""")
