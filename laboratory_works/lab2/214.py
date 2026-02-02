n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)

freq = {}
for num in sorted_a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
mx = -1
for num in sorted(freq):
    if freq[num] > mx:
        mx = freq[num]
        ans = num
print(ans)