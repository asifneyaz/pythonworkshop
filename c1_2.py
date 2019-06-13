# Unpacking elements from iterables of Arbitrary Length
record1 = ('Dave', 'dave@example.com', '02-22-19', '289-283-3231', '898-564-9876')
name, email, dob,  *phone_num = record1
print(name, email, dob, phone_num)

record2 = ('289-283-3231', '898-564-9876', 'Dave')
*phone_num2, name2 = record2
print(*phone_num2, name2)
print(phone_num2)

# example.py
#
# Unpacking of tagged tuples of varying sizes

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


fruits = ['mango', 'jackfruit']
for iter in fruits:
    print(iter)

line = 'fjdsjfk:ufdgs:/adsjf/dshjf:fdhjs'
s1, *s2, s3 = line.split(':')



