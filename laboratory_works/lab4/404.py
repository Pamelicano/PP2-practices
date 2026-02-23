def gen_sqr(a, b):
    for i in range(a, b+1):
        yield i*i

a, b = map(int, input().split())
buf = []
for x in gen_sqr(a, b):
    buf.append(str(x))
    if len(buf) == 1000:
        print("\n".join(buf), end="\n")
        buf.clear()

if buf:
    print("\n".join(buf))