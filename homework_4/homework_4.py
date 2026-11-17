my_dict = {
    'tuple': (1, 2, 3, 4, 5, 6),
    'list': [10, 15, 20, 30, 40, 50],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'sixseven': 67},
    'set': {10, 9, 8, 7, 6, 200}
}

#tuple
print(my_dict['tuple'][-1])

#list
my_dict['list'].append('bomboclat')
poped = (my_dict['list'].pop(1))
print(my_dict['list'])

#dict
my_dict['dict'] [('i am a tuple',)] = ('tuple1', 'tuple2', 'tuple3', 'tuple4', 'tuple5')
poped = my_dict['dict'].pop('sixseven')
print(my_dict['dict'])

#set
my_dict['set'].add(5)
my_dict['set'].remove(200)
print(my_dict['set'])

print(my_dict)
