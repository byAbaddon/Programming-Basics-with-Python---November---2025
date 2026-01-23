match input():
    case 'square':
        result = float(input()) ** 2
    case 'rectangle':
        result = float(input()) * float(input())
    case 'circle':
        result = float(input()) ** 2 * 3.14159
    case 'triangle':
        result = float(input()) * float(input()) / 2

print(f'{result:.3f}')
