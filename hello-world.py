from humansize import approximate_size


def testy(msg):
    '''
    Do something
    '''
    print(msg)


testy('Hello, World!')
print(approximate_size(4000, False) + '\n')

print('Documentation block: ')
print('\t' + approximate_size.__doc__ + '\n')

print('Name of module:')
print('\t' + approximate_size.__name__ + '\n')
