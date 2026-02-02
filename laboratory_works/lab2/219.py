n = int(input())
freq = {}
for _ in range(n):
    s = input()
    name, number = s.split()
    freq[name] = freq.get(name, 0) + int(number)
for key in sorted(freq):
    print(key, freq[key])
