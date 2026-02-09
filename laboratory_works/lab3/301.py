n = input()

for c in n:
    if c.isdigit():
        if int(c) % 2 != 0:
            print("Not valid")
            break
else:
    print("Valid")