s = input()
vowels = 'aeiouAEIOU'
if any(map(lambda x: x in vowels, s)):
    print("Yes")
else:
    print("No")