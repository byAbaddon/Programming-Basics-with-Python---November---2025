s = input()

fruit = ('banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes')
vegetable = ('tomato', 'cucumber', 'pepper', 'carrot')

print('fruit' if s in fruit else 'vegetable' if s in vegetable else 'unknown')
