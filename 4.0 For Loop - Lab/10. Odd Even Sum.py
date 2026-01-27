# l = r = c = 0
# for x in [int(input()) for _ in range(int(input()))]:
#
#     if c & 1:
#         l += x
#     else:
#         r += x
#     c += 1
#
# print(f'Yes\nSum = {l}' if l == r else f'No\nDiff = {abs(r - l)}')



s = [0, 0]
for i in range(int(input())):
    s[i & 1] += int(input())

print(f'Yes\nSum = {s[0]}' if s[0] == s[1] else f'No\nDiff = {abs(s[1] - s[0])}')


