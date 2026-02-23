import json
import re

data = json.loads(input())
q = int(input())

pattern = re.compile(r'\.?([a-zA-Z_]\w*)|\[(\d+)\]')
NOT_FOUND = object()

def resolve(obj, query):
    cur = obj
    pos = 0
    for m in pattern.finditer(query):
        if m.start() != pos:
            return NOT_FOUND
        pos = m.end()
        key, ind = m.groups()

        if key is not None:
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                return NOT_FOUND
        else:
            idx = int(ind)
            if isinstance(cur, list) and 0 <= idx < len(cur):
                cur = cur[idx]
            else:
                return NOT_FOUND
    if pos != len(query):
        return NOT_FOUND
    return cur


for _ in range(q):
    query = input().strip()
    result = resolve(data, query)

    if result is NOT_FOUND:
        print("NOT_FOUND")
    else:
        print(json.dumps(result, separators=(',', ':')))