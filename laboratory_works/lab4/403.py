def gen_div(n):
    for i in range(0, n + 1, 12):
        yield i

n = int(input())

buf = []
for x in gen_div(n):
    buf.append(str(x))
    if len(buf) == 1000:
        print(" ".join(buf), end=" ")
        buf.clear()

if buf:
    print(" ".join(buf))