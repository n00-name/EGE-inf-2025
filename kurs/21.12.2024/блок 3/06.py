def f(start, count, ans):
    if count == 4:
        ans.add(start)
        return 1
    elif count > 4:
        return 0
    else:
        return f(start + 1, count + 1, ans) + f(start + 5, count + 1, ans) + f(start * 3, count + 1, ans)


ans = set()
f(1, 0, ans)
print(len(ans))