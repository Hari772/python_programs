Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
h={1:"one",2:"two",3:"three",4:"four",5:"five"}
h
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
type(h)
<class 'dict'>
len(h)
5
all(h)
True
any(h)
True
sorted(h)
[1, 2, 3, 4, 5]
h.update(6:"six")# dict_name.update(dict_name2)
SyntaxError: invalid syntax
h.update({6:"six",7:"Seven"})
h
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'Seven'}

