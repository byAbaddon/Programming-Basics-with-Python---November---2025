speed = float(input())
print('slow' if speed <= 10 else 'average' if speed <= 50 else 'fast' if speed <= 150 \
    else 'ultra fast' if speed <= 1000 else 'extremely fast')