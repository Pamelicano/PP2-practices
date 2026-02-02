n = int(input())
a = []
for _ in range(n):
    num = int(input())
    a.append(num)   
freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
count = 0
for num in freq:
    if freq[num] == 3:
        count += 1
print(count)
