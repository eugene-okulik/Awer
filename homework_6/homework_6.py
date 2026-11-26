text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,'
        ' facilisis vitae semper at, dignissim vitae libero')

words = text.split()
ending = 'ing'
for word in words:
    if word.endswith(','):
        print(f'{word.replace(',', '')}{ending}, ', end='')
    elif word.endswith('.'):
        print(f'{word.replace('.', '')}{ending}. ', end='')
    else:
        print(f'{word}{ending} ', end='')
print()

numbers = list(range(1, 101))
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz')
    elif number % 3 == 0:
        print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
