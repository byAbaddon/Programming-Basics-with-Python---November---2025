lst =sorted([int(input()) for _ in range(int(input()))])
big_n = lst.pop()
sum_n = sum(lst)

print(f'Yes\nSum = {big_n}' if sum_n == big_n else f'No\nDiff = {abs(sum_n - big_n)}')
