def cycle_list(lst, k):
    for _ in range(k):
        for item in lst:
            yield item
lst = list(map(str, input().split()))
k = int(input())    
for item in cycle_list(lst, k):
    print(item, end = " ")
