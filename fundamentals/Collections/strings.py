# Strings are a sequence of unicode code points

string1 = 'This is a string'
string2 = "This is also a string"

path = r"\Users\tousif\python"

print(path)

print('\u0534') # unicode
print('\xe5')   # hexadecimal
print('\345')   # octal

"""
call the join() method on the separator string
"""

colors = ';'.join(['#45fggf', '#45sdf4', '#984334'])

print(colors)

print(colors.split(';'))

"""
To concatenate
invoke join on empty text
Some for nothing
"""

joined_string = "".join(['way', 'land'])
print(joined_string)

departure, separator, arrival = "London:Edinburgh".partition(":")

print(departure, separator, arrival)

origin, _, destination = "Seattle-Boston".partition('-')

print(destination)
print('Current position is {latitude} {longitude}'.format(latitude='60N', longitude='5E'))

print('Current position is {} {}'.format('60N', '5E'))

print('Current position is {latitude} {longitude}'.format(longitude='5E', latitude='60N'))
