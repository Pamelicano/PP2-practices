import math
import sys

def read_input():
    try:
        r = float(sys.stdin.readline().strip())
        x1, y1 = map(float, sys.stdin.readline().strip().split())
        x2, y2 = map(float, sys.stdin.readline().strip().split())
        return r, x1, y1, x2, y2
    except:
        sys.exit(1)


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def is_segment_intersecting_circle(r, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    a = dx * dx + dy * dy
    b = 2 * (x1 * dx + y1 * dy)
    c = x1 * x1 + y1 * y1 - r * r

    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return False

    t1 = (-b - math.sqrt(discriminant)) / (2 * a)
    t2 = (-b + math.sqrt(discriminant)) / (2 * a)

    if (0 <= t1 <= 1) or (0 <= t2 <= 1):
        return True

    return False


def shortest_path(r, x1, y1, x2, y2):
    direct = distance(x1, y1, x2, y2)

    if not is_segment_intersecting_circle(r, x1, y1, x2, y2):
        return direct

    d1 = distance(0, 0, x1, y1)
    d2 = distance(0, 0, x2, y2)

    angle1 = math.acos(r / d1)
    angle2 = math.acos(r / d2)

    total_angle = math.acos(
        (x1 * x2 + y1 * y2) / (d1 * d2)
    )

    arc_angle = total_angle - angle1 - angle2

    tangent1 = math.sqrt(d1 * d1 - r * r)
    tangent2 = math.sqrt(d2 * d2 - r * r)

    arc_length = r * arc_angle

    return tangent1 + arc_length + tangent2


r, x1, y1, x2, y2 = read_input()
result = shortest_path(r, x1, y1, x2, y2)
print("{:.10f}".format(result))

