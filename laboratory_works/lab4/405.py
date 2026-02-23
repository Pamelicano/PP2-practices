def gen_sqr(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
buf = []
for x in gen_sqr(n):
    buf.append(str(x))
    if len(buf) == 1000:
        print("\n".join(buf), end="\n")
        buf.clear()

if buf:
    print("\n".join(buf))