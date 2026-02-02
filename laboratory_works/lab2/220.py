import sys
input = sys.stdin.readline

n = int(input())
book = {}
output = []
for _ in range(n):
    parts = input().split()
    command = parts[0]
    if (command == "set"):
        book[parts[1]] = parts[2]
    elif (command == "get"):
        key = parts[1]
        if key in book:
            output.append(book[key])
        else:
            output.append(f"KE: no key {key} found in the document")


print("\n".join(output))
