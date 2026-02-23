def gen(n):
    for i in range(0, n+1):
        yield 2**i
n = int(input())
buf = []
for x in gen(n):
    buf.append(str(x))
    if len(buf) == 1000:
        print(" ".join(buf), end=" ")
        buf.clear()
if buf:
    print(" ".join(buf))