# WAP to enter any number and display it in words.
# Ex 123 - One Two Three

num = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
       '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero'}

n = input('Enter a number: ')
num_in_word = ''
for i in n:
    for keys, values in num.items():
        if i == keys:
            num_in_word += f'{values} '

print(f'This {n} in Words: {num_in_word}')
