def helloWorld(name, emoji):
    print(f'Hello World! by {name} {emoji}')


helloWorld('Manikandan', ':)')


def funcWithArgs(*args, **kargs):
    return sum(args) + sum(kargs.values())


print(funcWithArgs(1, 2, 3, 4, 5, num1=5, num2=10))


def highestEven(li):
    maxEven = 0
    for element in li:
        if element % 2 == 0:
            maxEven = maxEven if maxEven > element else element
    return maxEven


print(highestEven([10, 2, 3, 4, 8, 11]))

def sum():
    return 'asd'

print(sum())
a = 'asdasdasdasdoo'
print(a[:-1])