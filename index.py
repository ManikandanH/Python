# # name = input('Enter your Name: ')
# # age = input('Enter your age: ')

# # # formatted strings
# # #python3 syntax(recommended approach)
# # print(f'Hi {name}. You are {age} years old')
# # #python2 syntax
# # print('Hi {}. You are {} years old'.format(name, age))


# # #dictionary

# # dictionary = {
# #     '[100]': 'Hello'
# # }

# # print(dictionary.keys())

# #counter

# myList = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for item in myList:
#     sum += item
# print(sum)

# for index, value in enumerate(list(range(100))):
#     if index==50:
#         print(value)

data = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
str = ''

for i in data:
    for j in i:
        if j == 0:
            str += ' '
        else:
            str += '*'
    str += '\n'

print(str)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# print(some_list[1:])
index = 0
for i in some_list:
    for j in some_list[index + 1:]:
        if i == j:
            print(i)
    index += 1
