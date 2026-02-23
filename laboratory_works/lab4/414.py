from datetime import datetime, timedelta

def parse_dt(s):
    date_p, tz_p = s.split()
    dt = datetime.strptime(date_p, "%Y-%m-%d")

    sign = 1 if tz_p[3] == '+' else -1
    h, min = map(int, tz_p[4:].split(":"))
    offset = timedelta(hours=h, minutes=min) * sign
    return dt - offset


d1 = parse_dt(input().strip())
d2 = parse_dt(input().strip())

diff = abs(d1 - d2)
print(diff.days)