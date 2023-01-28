#あいさつ表示
print("Hello!")

#あいさつと名前の入力を表示
def helloworld():
    name = input('input your name: ')
    message = 'Hello ' + name + ' !'
    print(message)

helloworld()

#九九表示
result = [[f'{num1 * num2:2}' for num2 in range(1, 10)] for num1 in range(1, 10)]

for row in result:
    print(', '.join(row))