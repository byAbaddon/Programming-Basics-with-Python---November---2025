target_jump = int(input())

start_jump = target_jump - 30
count_jump = fail_jump = 0

while target_jump >= start_jump:
    jump = int(input())
    count_jump += 1

    if jump <= start_jump:
        fail_jump += 1
        if fail_jump == 3:
            print(f'Tihomir failed at {start_jump}cm after {count_jump} jumps.')
            exit()
    else:
        fail_jump = 0
        start_jump += 5

print(f'Tihomir succeeded, he jumped over {target_jump}cm after {count_jump} jumps.')
