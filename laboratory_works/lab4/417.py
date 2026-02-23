import math

R = int(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx**2 + dy**2
b = 2 * (dx*(x1) + dy*(y1))
c = (x1)**2 + (y1)**2 - R**2
D = b**2 - 4*a*c

if D < 0:
    print("0.0000000000")
else:
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD) / (2*a)
    t2 = (-b + sqrtD) / (2*a)
    t_in = max(0.0, min(t1, t2))
    t_out = min(1.0, max(t1, t2))
    if t_in > t_out:
        print("0.0000000000")
    else:
        length = math.sqrt(dx**2 + dy**2) * (t_out - t_in)
        print(f'{length:.10f}')