def example(string, number):
    return string, number

print(example('John', 30))

def example(string= 'Mark', number=45):
    return string, number

print(example())

example = [1,2,3]
del(example[0])
print(example)

for x in example:
    print(x)

example = {}
example[1] = "whatever"
print(example)
