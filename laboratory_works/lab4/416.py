from datetime import datetime, timedelta, timezone
import sys

def parse_line(s):
    s = s.strip()
    dt_part, tz_part = s.rsplit(maxsplit=1)  
    dt = datetime.strptime(dt_part, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz_part[3] == '+' else -1
    hh = int(tz_part[4:6])
    mm = int(tz_part[7:9])
    tz = timezone(sign * timedelta(hours=hh, minutes=mm))
    local_dt = dt.replace(tzinfo=tz)
    return local_dt.astimezone(timezone.utc)

start_utc = parse_line(sys.stdin.readline())
end_utc = parse_line(sys.stdin.readline())
duration_seconds = int((end_utc - start_utc).total_seconds())
print(duration_seconds)