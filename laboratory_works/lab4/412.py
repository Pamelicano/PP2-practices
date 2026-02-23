import json

def diff(obj1, obj2, path=""):
    diffs = []

    keys = set(obj1.keys()) | set(obj2.keys())

    for key in keys:
        new_path = f"{path}.{key}" if path else key

        in1 = key in obj1
        in2 = key in obj2

        if in1 and in2:
            v1 = obj1[key]
            v2 = obj2[key]

            if isinstance(v1, dict) and isinstance(v2, dict):
                diffs.extend(diff(v1, v2, new_path))
            else:
                if v1 != v2:
                    diffs.append((new_path, v1, v2))

        elif in1 and not in2:
            diffs.append((new_path, obj1[key], "<missing>"))

        elif not in1 and in2:
            diffs.append((new_path, "<missing>", obj2[key]))

    return diffs


obj1 = json.loads(input())
obj2 = json.loads(input())

differences = diff(obj1, obj2)

if not differences:
    print("No differences")
else:
    differences.sort(key=lambda x: x[0])
    for path, old, new in differences:
        if old != "<missing>":
            old = json.dumps(old, separators=(',', ':'))
        if new != "<missing>":
            new = json.dumps(new, separators=(',', ':'))

        print(f"{path} : {old} -> {new}")