# heterogeneous mutable sequences of objects

# lists can be heterogeneous wrt the type of the objects
a = ['apple', 8, 'banana']

charactersList = list('charachters')
print(charactersList)

"""
Idiom for copying lists
full_slice = seq[:]
"""


class Student:

    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return self.name


b = a[:]

print(a == b)
print(a is b)

mark = Student('Mark')
james = Student('James')
msg = "Hello"

listA = [msg, mark, james]

listB = listA[:]

print(listB is listA)

listB[1].set_name('Ryan')

print(listA)
print(listB)

print(listA[1])
print(listB[1])

"""
Other ways of copying lists:
copy() method
list() constructor

Note: all the copy methods described above perform a shallow copy
i.e. the object references inside the list, refer to the same objects
"""

listC = listA.copy()

listD = list(listB)  # most preferable, as it works with other collections too

# Repetition is shallow
s = [[-1, 1]] * 5
print(s)

s[3].append(7)
print(s)

"""
del seq[index] to remove by index
seq.remove(item) to remove by value; raises ValueError if not present

remove(item) is equivalent to del seq[seq.index(item)]
"""

msg = 'I accidently the whole universe'
words = msg.split()
words.insert(2, 'destroyed')
print(words)
new_msg = " ".join(words)
print(new_msg)

k = [23, 45, 56, 76, 99]
print(id(k))

k += [45, 75, 34, 69]
print(id(k))

k.extend([34, 23, 65, 32, 67, 12])
print(k)
print(id(k))

k = [83, 47]
print(id(k))

h = 'A quick brown fox jumped over the lazy dog'.split()
h.sort(key=len)
print(h)

h.reverse()
print(h)

h = 'A quick brown fox jumped over the lazy dog'.split()
h.sort(reverse=True, key=len)
print(h)

"""
sorted() built-in function sorts any iterable series and return a list

reversed() built-in function reverses any iterable series
returns a reverse iterator
"""

x = [1, 7, 3, 8, 2, 9]

y = sorted(x, reverse=True)
print(x)
print(y)

z = reversed(x)
print(type(z))
print(list(z))