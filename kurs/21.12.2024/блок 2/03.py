def f(start, count, ans):
    if count == 12:
        ans.add(start)
        return 1
    elif count > 12:
        return 0
    else:
        return f(start + 1, count + 1, ans) + f(start * 2 - 3, count + 1, ans)


ans = set()
f(3, 0, ans)
print(len(ans))
