file = open('hello.txt', encoding='utf-8')

hello = file.read()

print(file)
print(hello)

file.close()

hello2 = open('hello.txt', encoding='utf-8', mode='a')

hello2.write('success!\n')
