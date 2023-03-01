def sum(lst):
    s = 0
    for i in lst:
        s += i
    return s

lst = [1,2,3,4,5]
ans = sum(lst)
print(ans)