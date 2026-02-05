days, hours = int(input()), int(input())
total = 0

for d in range(1, days + 1):
    subtotal = 0
    for h in range(1, hours + 1):
        if d % 2:
            subtotal += 1 if h & 1 else 1.25
        else:
            subtotal += 2.5 if h & 1 else 1
    print(f'Day: {d} - {subtotal:.2f} leva')
    total += subtotal

print(f'Total: {total:.2f} leva')

# -----------------------------------------------------------
# days = int(input())
# hours = int(input())
# total = subtotal = 0
#
# for d in range(1, days + 1):
#     for h in range(1, hours + 1):
#         if d & 1:
#             if h & 1:
#                 subtotal += 1
#             else:
#                 subtotal += 1.25
#         else:
#             if h & 1:
#                 subtotal += 2.50
#             else:
#                 subtotal += 1
#
#     print(f'Day: {d} - {subtotal:.2f} leva')
#     total += subtotal
#     subtotal = 0
#
# print(f'Total: {total:.2f} leva')
